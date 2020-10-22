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
impl Default for Event {
  fn default () -> Event {
      Event { id: 0, link: " ".to_string(), title:" ".to_string(), img:" ".to_string()}
  }
}


#[derive(Serialize)]
struct JsonApiResponseByVec {
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
fn get_event_by_id(id: i32,conn:DbConn) -> Json<Event>  {
  let mut event_to_send = Event::default();
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
         event_to_send=event;}
      Json(event_to_send)
}

#[get("/getallevent")]
fn get_all_event(conn:DbConn) -> Json<JsonApiResponseByVec> {

  let mut response = JsonApiResponseByVec {data: vec![], };
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
    .mount("/", routes![get_all_event,get_event_by_id])
    .launch();
}
