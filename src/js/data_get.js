async function data_get(p_name) {
    let data = await eel.data_get(p_name)()
    return data
}