import axios from "axios"

export function fetchPost(url, data) {
  return axios.post(url, data) ;
}