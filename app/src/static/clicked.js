function good(ele){
	var all_word = document.getElementsByClassName('tweet');
	var id_value = ele.id;  // ボタンのidナンバーを取得  
	var word = all_word[id_value]; //目的のツイートを取得
	console.log(word.innerHTML); 
	word.style.fontSize = '120%';
};

function bad(ele){
	var all_word = document.getElementsByClassName('tweet');
	var id_value = ele.id;  // ボタンのidナンバーを取得  
	var word = all_word[id_value]; //目的のツイートを取得
	console.log(word.innerHTML); 
	word.style.fontSize = '80%';
};
