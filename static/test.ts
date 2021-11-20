import {echo} from "./app.js"

const base = "http://localhost:8080/"
const urls = [base, base + "echo/Hello", base + "not-found"]
for (let url of urls) {
    echo(url)
    .then(function(text: string) {console.log(url, text)})
    .catch(error => {
        console.error("failed to get ${url}")
    })
}
