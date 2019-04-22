function generate(keyword)
{
    const request = new XMLHttpRequest();
    request.open("GET",`m.liveatc.net/feeds/?icao=${keyword}`);
    request.addEventListener(
        "load",(event) =>
    {
        document.write(event.target.responseText);
        console.log(event.target.responseText);
    })
    request.send();
}
generate("NRT");