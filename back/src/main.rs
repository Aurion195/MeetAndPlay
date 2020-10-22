#![feature(decl_macro)]
#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
use serde::{Deserialize, Serialize};
extern crate rocket_cors;

use rocket_contrib::json::Json;
use rocket_contrib::databases::rusqlite::Connection;
use rocket::http::Method; // 1.

use rocket_cors::{
    AllowedHeaders, AllowedOrigins, Error, // 2.
    Cors, CorsOptions // 3.
};

#[database("db")]
struct DbConn(Connection);

#[derive(Debug,Serialize, Deserialize,)]
struct Event {
    id: i32,
    link: String,
    title: String,
    img: String
}

#[derive(Serialize)]
struct JsonApiResponse {
    data: Vec<Event>,
}


fn make_cors() -> Cors {
    let allowed_origins = AllowedOrigins::some_exact(&[ // 4.
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:8000",
        "http://0.0.0.0:8000",
    ]);

    CorsOptions { // 5.
        allowed_origins,
        allowed_methods: vec![Method::Get].into_iter().map(From::from).collect(), // 1.
        allowed_headers: AllowedHeaders::some(&[
            "Authorization",
            "Accept",
            "Access-Control-Allow-Origin", // 6.
        ]),
        allow_credentials: true,
        ..Default::default()
    }
    .to_cors()
    .expect("error while building CORS")
}
#[get("/geteventbyid/<id>")]
fn geteventbyid(id: i32,conn:DbConn) -> Json<JsonApiResponse>  {
  let mut response = JsonApiResponse { data: vec![], };
  let mut stmt = conn.prepare("SELECT id, link, title, img FROM events WHERE id=?").unwrap();
  let events = stmt.query_map(&[&id], |row|  {
          Event{
            id: row.get(0),
            link: row.get(1),
            title: row.get(2),
            img: row.get(3)
          }
        }).unwrap().map(|event| event.unwrap());//response
       for event in events {
         
         response.data.push(event);}
      Json(response)
}

#[get("/getallevent")]
fn getallevent(conn:DbConn) -> Json<JsonApiResponse> {
  
  let mut response = JsonApiResponse {data: vec![], };
  let mut stmt = conn.prepare("SELECT id, link, title, img FROM events").unwrap();
  let events = stmt.query_map(&[], |row|  {
          Event{
            id: row.get(0),
            link: row.get(1),
            title: row.get(2),
            img: row.get(3)
          }
        }).unwrap().map(|event| event.unwrap());//response
       for event in events {
         response.data.push(event);}
      Json(response)
}

fn main() {
  
    rocket::ignite()
    .attach(DbConn::fairing())
    .attach(make_cors()) // 7.
    .mount("/", routes![getallevent,geteventbyid])
    .launch();
}
