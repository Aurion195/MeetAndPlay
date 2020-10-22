#![feature(decl_macro)]
#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
use serde::{Deserialize, Serialize};
use rocket::{Request, Response};
use rocket::fairing::{Fairing, Info, Kind};
use rocket::http::{Header, ContentType, Method};
use std::io::Cursor;
use rocket_contrib::json::Json;
use rocket_contrib::databases::rusqlite::Connection;

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
pub struct CORS();

impl Fairing for CORS {
    fn info(&self) -> Info {
        Info {
            name: "Add CORS headers to requests",
            kind: Kind::Response
        }
    }

    fn on_response(&self, request: &Request, response: &mut Response) {
        if request.method() == Method::Options || response.content_type() == Some(ContentType::JSON) {
            response.set_header(Header::new("Access-Control-Allow-Origin", "*"));
            response.set_header(Header::new("Access-Control-Allow-Methods", "POST, GET, OPTIONS"));
            response.set_header(Header::new("Access-Control-Allow-Headers", "Content-Type"));
            response.set_header(Header::new("Access-Control-Allow-Credentials", "true"));
        }

        if request.method() == Method::Options {
            response.set_header(ContentType::Plain);
            response.set_sized_body(Cursor::new(""));
        }
    }
}

#[get("/geteventbyid/<id>")]
fn geteventbyid(id: i32,conn:DbConn) -> Json<JsonApiResponse>  {
  let mut response = JsonApiResponse {data: vec![], };
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
    .attach(CORS())
    .mount("/", routes![getallevent,geteventbyid])
    .launch();
}
