function show_msg() {
    document.querySelector('#msg').style.display = 'flex'
}

async function send_msg() {
    let text = document.querySelector('#msg-text').value
    await eel.send_msg(text)()
    console.log('message sent')
}