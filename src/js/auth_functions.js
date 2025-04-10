async function check_auth() {
    let is_auth = await eel.data_get('is_auth')()
    if (!is_auth) location.href = '/src/pages/auth.html'
}

async function exit_auth(force=false) {
    await eel.exit_auth(force)()
    // await check_auth()
}