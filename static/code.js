var moves = [];
var symbol = 'X';
var id = 0;

function sendRequest(moves){
            $.ajax({
                type: 'POST',
                url: '/moves',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ moves: moves }),
                dataType: 'json',
             })
}
function markbox(cell) {
    if (cell.value == '  ') {
        cell.value = symbol;
        document.getElementById(cell.id).style.color = 'red';
    }
    moves.push(cell.id);
    $.ajax({
        type: 'POST',
        url: '/moves',
        headers: { 'Content-Type': 'application/json' },
        data: JSON.stringify({ moves: moves }),
        dataType: 'json',
    })
        .done(function(res) {
            var pole = res.moves;
            var length = res.moves.length;
            moves = pole;
            if (pole[length - 1] < 0) {
                $('#' + id).removeClass('zlta');
                id = pole[pole.length - 2];
                $('#' + id).val('O');
                document.getElementById(id).style.color = 'blue';
                $('#' + id).addClass('zlta');
                setTimeout(function() {
                    switch (pole[length - 1]) {
                        case -1:
                            break;
                        case -2:
                        moves = [];
                            sendRequest(moves)
                            if (alert('Smola prehral si!')) {

                            } else window.location.reload();

                            break;
                        case -3:
                            alert('REMIZA');
                            break;
                    }
                }, 500);
            } else {
                $('#' + id).removeClass('zlta');
                id = pole[pole.length - 1];
                $('#' + id).val('O');
                $('#' + id).addClass('zlta');
                document.getElementById(id).style.color = 'blue';
                id = pole[pole.length - 1];
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
