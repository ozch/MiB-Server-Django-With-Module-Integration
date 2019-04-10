var shark_flows;
var RequestingPacketFlow = setInterval(async function () {
    $.ajax({
        url:'/api/flowshark/',
        dataType: 'json',
        method: 'GET',
        async: false,
        success: function (json) {
            console.log(json)
            shark_flows = json;
        }

    });
    console.log("Ran");
    while (shark_flows.length != 0) {
        temp = shark_flows.shift();
        $('table > tbody > tr:first')
            .before("<tr><td scope='row'>" + temp['start'] + "</td> <td>" + temp['src_port'] + "</td> <td>" + temp['end'] + "</td> <td>" + temp['dest_port'] + "</td> <td>" + temp['reporter'] + "</td> <td>" + temp['pkts'] + "</td> <td>" + temp['bytes'] + "</td></tr>");

    }
}, 3000);