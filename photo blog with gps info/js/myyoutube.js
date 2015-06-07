
function setbold(event){
    console.log('set')
    if (event.data===1 || event.data===2 || event.data===3){
        var index=uindex();
        console.log('set '+index);
        var docu=document.getElementById('song'+index.toString());
        docu.style.fontSize="150%";
    }
}


function make_play_list(str) {

        player = new YT.Player('playerLayer', {
            height: '300',
            width: '500',
            playerVars: {
                'autoplay': 0,  // 자동실행여부
                'controls': 0,   // 재생컨트롤 노출여부
                'autohide': 0,  // 재생컨트롤이 자동으로 사라질지의 여부
                'rel': 0, 
                'wmode': 'transparent',
                'playlist':str
            },
            events: {
                'onStateChange':setbold
            }
        });
}


function uplay(){
    unsetbold();
    player.playVideo();
}

function ustop(){
    player.stopVideo();
}

function upause(){
    player.pauseVideo();
}

function unext(){
    unsetbold();
    player.nextVideo();
}

function upre(){
    unsetbold();
    player.previousVideo();
}

function uplay_num(num){
    player.playVideoAt(num);
}

function uindex(){
    var tmp=player.getPlaylistIndex()+1;
    return tmp;
}

function unsetbold(){
    var index=uindex();
    console.log('unset '+index);
    var docu=document.getElementById('song'+index.toString());
    docu.style.fontSize="100%";
}