async function createMemo(value){
    const res = await fetch("/memos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: new Date(),
            content: value
        }),
    });

    const jsonRes = await res.json();
    console.log(jsonRes)
}

function handleSubmit(e){
    e.preventDefault();
    const input = document.querySelector('#memo-input')
    createMemo(input.value)
    input.value=''
}

const form = document.querySelector('#memo-form')
form.addEventListener("submit", handleSubmit)