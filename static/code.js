var moves = [];
var values = [];
var symbol = 'X';
var id = 0;

(function(d,b){if(!d.exponea){var a=function(a,g){function k(c){return function(){var e=arguments;""==a&&"initialize"==c&&e&&e[0].modify&&e[0].modify.overlay&&"loading"==b.readyState&&(b.write('<div id="__inf__overlay__" style="position:absolute;background:#fff;left:0;top:0;width:100%;height:100%;z-index:1000000"></div>'),setTimeout(function(){var a=b.getElementById("__inf__overlay__");a&&b.body.removeChild(a);res.__=!0},e[0].modify.delay||500));d.exponea._.push([a+c,arguments])}}var h=g.split(" "),f,c;res={_:[]};for(c=0;c<h.length;c++)f=h[c],res[f]=k(f);return res};d.exponea=a("","initialize identify update track trackLink trackEnhancedEcommerce getHtml showHtml showBanner showForm ping getAbTest");d.exponea.notifications=a("notifications.","isAvailable isSubscribed subscribe unsubscribe");var a=b.createElement("script"),g="https:"===b.location.protocol?"https:":"http:";a.type="text/javascript";a.async=!0;a.src=g+"//api.exponea.com/js/exponea.min.js";b.getElementsByTagName("head")[0].appendChild(a)}})(window,document);
    exponea.initialize({
        "token": "fc4f30dc-90c7-11e8-88f7-14187733e19e",
        "track": {
            "visits": true
        }
        //, customer: window.loggedInCustomer // replace window.loggedInCustomer with id of your web site customer, e.g. "john.smith@gmail.com"
});

function sendRequest(moves, val){
            $.ajax({
                type: 'POST',
                url: '/moves',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ moves: moves, values: val }),
                dataType: 'json',
             })
}


function markbox(cell) {
    if (cell.value == '  ') {
        cell.value = symbol;
        document.getElementById(cell.id).style.color = 'red';
    }
    else {
        alert("Obsadene co nevidis?");
    }
    moves.push(cell.id);
    if (moves.length == 1) {
        var val = new Array(10);
        for (var i = 0; i < 10; i++) {
            val[i] = new Array(10);
            for (var j = 0; j < 10; j++) {
                val[i][j] = 0;
            }
        }
        console.log("Values: ", val);
    }


    $.ajax({
        type: 'POST',
        url: '/moves',
        headers: { 'Content-Type': 'application/json' },
        data: JSON.stringify({ moves: moves, values: values}),
        dataType: 'json'
    })
        .done(function(res) {
            var pole = res.moves[0];
            var val = res.moves[1];
            var length = res.moves[0].length;
            console.log("RESPONSE:", res)
            console.log("POLE", pole);
            values = val;
            moves = pole;
                console.log(pole[length - 1]);
            if (pole[length - 1] < 0) {
                $('#' + id).removeClass('zlta');
                id = pole[pole.length - 2];
                $('#' + id).val('O');
                document.getElementById(id).style.color = 'blue';
                $('#' + id).addClass('zlta');

                setTimeout(function() {
                    switch (pole[length - 1]) {
                        case -1:
                            moves = [];
                            val = [];
                            var val = new Array(10);
                            for (var i = 0; i < 10; i++) {
                                val[i] = new Array(10);
                                for (var j = 0; j < 10; j++) {
                                    val[i][j] = 0;
                                }
                            }
                            sendRequest(moves, val);
                            if (alert('Gratulujeme vyhral si!')) {
                            } else window.location.reload();

                            break;
                        case -2:
                            console.log("Smola");
                            moves = [];
                            val = [];
                            var val = new Array(10);
                            for (var i = 0; i < 10; i++) {
                                val[i] = new Array(10);
                                for (var j = 0; j < 10; j++) {
                                    val[i][j] = 0;
                                }
                            }
                            sendRequest(moves, val);
                            if (alert('Smola prehral si!')) {
                            } else window.location.reload();

                            break;
                        case -3:
                            moves = [];
                            val = [];
                            var val = new Array(10);
                            for (var i = 0; i < 10; i++) {
                                val[i] = new Array(10);
                                for (var j = 0; j < 10; j++) {
                                    val[i][j] = 0;
                                }
                            }
                            sendRequest(moves, val);
                            if (alert('Smola REmiza!')) {
                            } else window.location.reload();

                            break;
                    }
                }, 500);
            } else {
                $('#' + id).removeClass('zlta');
                id = pole[pole.length - 1];
                if ( $('#' + id).value == '  ') {
                    $('#' + id).val('O');
                    $('#' + id).addClass('zlta');
                    document.getElementById(id).style.color = 'blue';
                    id = pole[pole.length - 1];
                }
                else {
                    alert("Toto policko je uz obsadene nevidis?!")
                }
            }
        })
        .fail(function(err) {
            console.log(err);
        });
}

function run() {
    table(10);
    console.log(moves);
    for (var i = 0; i < 10; i++) {
        console.log('player x in on the move');
    }
}

function table(n) {
    var pos = 0;
    document.write('<table class=tabulka>');
    for (var a = 0; a < n; a++) {
        document.write('<tr>');
        for (var b = 0; b < n; b++) {
            pos = a * n + b;
            document.write(
                '<td>' +
                    '<input id=' +
                    pos +
                    ' type=button value="  " onclick= markbox(this) class=button>' +
                    '</td>',
            );
        }
        document.write('</tr>');
    }
    document.write('<table>');
}

run();
