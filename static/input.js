function exec() {
  const speech = new webkitSpeechRecognition();
  speech.lang = 'ja-JP';

  const input = document.getElementById('rawtext');

  speech.start();
  speech.addEventListener('result' , function(e) {
    //console.log(e);
    const text = e.results[0][0].transcript;
    input.value = text;
  });
}
