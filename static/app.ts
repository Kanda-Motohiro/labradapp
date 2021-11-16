/*
 * app.ts by kanda.motohiro@gmail.com. Released under GPL v3.
 */
console.log("app.ts loaded")

function echo(url: string) :Promise<string> {
    return fetch(url)
    .then(function(response: Response) {
        if (response.ok) {
            return response.text()
        }
        throw new Error(response.statusText)
    })
}

async function onClick(input_id: string, path: string, output_id: string) :Promise<void> {
	// ここに書かれたものを、
    const input:HTMLInputElement = <HTMLInputElement>document.getElementById(input_id)
	// ここにエコーバックして出す。
    const output = document.getElementById(output_id)
    if (input == null || output == null) {
        console.log("id not found", input_id, output_id)
        return
    }
    const data = input.value

    const url = document.location.origin + "/" + path + "/" + data
    console.log(url)

	const out = await echo(url)
	output.innerHTML = out
}

function button0() :void {
    console.log("button0");
    onClick("input0", "echo", "label0")
}

function button1() :void {
    console.log("button1");
	// こっちが、非同期。
    onClick("input1", "aecho", "label1")
}

window.addEventListener('load', () => {
    console.log("load")
    let el0 = document.getElementById("button0")
    let el1 = document.getElementById("button1")
    if (el0 == null || el1 == null) {
        console.error("element not found", el0, el1)
        return
    }
    el0.addEventListener('click', button0)
    el1.addEventListener('click', button1)
})
