function player() {
    let i = $('#'),
        audioFile = audioList[1],
        bTime,
        nTime = 0,
        buffInterval = null;

    function playPause() {
        if (audio.paused) {
            checkBuffering()
            i.attr("class", "fas fa-pause")
            audio.play();
        } else {
            clearInterval(buffInterval);
            i.attr("class", "fas fa-play");
            audio.pause();
        }
    }

    function onKeyDown(event) {
        switch (event.keyCode) {
            case 32: //SpaceBar
                if (audio.paused) {
                    checkBuffering();
                    i.attr("class", "fas fa-pause");
                    audio.play();
                } else {
                    clearInterval(buffInterval);
                    i.attr("class", "fas fa-play");
                    audio.pause();
                }
                break;
        }
        return false;
    }

    window.addEventListener("keydown", onKeyDown, false);

    function checkBuffering() {
        clearInterval(buffInterval);
        buffInterval = setInterval(function player() {
            bTime = new Date();
            bTime = bTime.getTime();
        }, 100);
    }

    function selectTrack() {
        audio.src = audioFile;

        nTime = 0;
        bTime = new Date();
        bTime = bTime.getTime();
    }

    function initPlayer() {
        audio = new Audio();

        selectTrack()
        playPause()
    }

    initPlayer()

}
