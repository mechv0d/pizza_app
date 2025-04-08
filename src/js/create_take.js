async function create_take(tid, uid, sname, name, lname, status, st_time, end_time, place, closed) {
    let shifter = await eel.create_take(tid, uid, sname, name, lname, status, st_time, end_time, place, closed)()
    return shifter
}