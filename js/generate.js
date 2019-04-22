generate(keyword)
{
    const request = new XMLHttpRequest();
    request.open("GET",`http://m.liveatc.net/feeds/?icao=${keyword}`);
    request.addEventListener(
        "load",(event) =>
    {
        document.write(event.target.responseText);
    })
    request.send();
}
generate("NRT");