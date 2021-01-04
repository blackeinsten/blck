<?php 
	$chat_id = "xxxxxxxxx"; //chatID
	$bot_url    = "https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/"; //Bot Token dari BotFather
	$url        = $bot_url . "sendDocument?chat_id=" . $chat_id ;

	$post_fields = array(
	    'document'     => new CURLFile(realpath("yourfile")) //File di folder lokal. cth : *.pdf, *.xls, *.doc, etc.
	);

	$ch = curl_init(); 
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(
	    "Content-Type:multipart/form-data"
	));
	curl_setopt($ch, CURLOPT_URL, $url); 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
	curl_setopt($ch, CURLOPT_INFILESIZE, filesize(realpath("yourfile")));
	$output = curl_exec($ch);

 ?>