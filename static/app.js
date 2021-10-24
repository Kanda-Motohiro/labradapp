/*
 * app.js by kanda.motohiro@gmail.com. Released under GPL v3.
 */
console.log("app.js loaded");

function echo(input_id, path, output_id) {
	// ここに書かれたものを、
    let input = document.getElementById(input_id)
    data = input.value
	// ここにエコーバックして出す。
    let output = document.getElementById(output_id)

    let url = document.location.origin + "/" + path + "/" + data
    console.log(url)

	// これが、非同期 http get だそうな。see MDN.
    fetch(url)
    .then(function(response) {
        if (response.ok) {
            return response.text()
        }
        throw new Error(response.status)
    })
    .then(function(text) {
        console.log(text)
        output.innerHTML = text
    })
    .catch(error => {
        console.error(error)
    })
}

function button0() {
    console.log("button0");
    echo("input0", "echo", "label0")
 }

 function button1() {
    console.log("button1");
	// こっちが、非同期。
    echo("input1", "aecho", "label1")
 }
