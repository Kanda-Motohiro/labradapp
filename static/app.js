/*
 * app.js by kanda.motohiro@gmail.com. Released under GPL v3.
 */
console.log("app.js loaded");

async function onClick(input_id, path, output_id) {
	// ここに書かれたものを、
    let input = document.getElementById(input_id)
    data = input.value
	// ここにエコーバックして出す。
    let output = document.getElementById(output_id)

    let url = document.location.origin + "/" + path + "/" + data
    console.log(url)

	out = await echo(url)
	output.innerHTML = out
}

function echo(url) {
    return fetch(url)
    .then(function(response) {
        if (response.ok) {
            return response.text()
        }
        throw new Error(response.status)
    })
}

function button0() {
    console.log("button0");
    onClick("input0", "echo", "label0")
 }

 function button1() {
    console.log("button1");
	// こっちが、非同期。
    onClick("input1", "aecho", "label1")
 }
