/*export async function fetchPost(url, data) {
        const res = await fetch(
          url, {
            method: "POST",
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
            },
            body: JSON.stringify(data),
          })
          return res ;
      }*/
import axios from "axios"
export function fetchPost(url, data) {
  return axios.post(url, data) ;
}