$(function(){

    
    $('#keywordsubmit').click(function(){
		
		var search_topic = $('#keyword').val();

        console.log(search_topic)
		
				
		if (search_topic){
                chrome.runtime.sendMessage(
					{topic: search_topic},
					function(response) {
                        console.log("15")
						result = response.farewell;
						// alert(result.summary);
						
						var notifOptions = {
                            title: "Summarization",
                            // iconUrl: "http://www.google.com/favicon.ico",
                            iconUrl: "images/icon.png",
							type: "basic",
							message: result.summary
						};
						chrome.notifications.create('WikiNotif1', notifOptions);

                        var notifOptions = {
                            title: "Keywords",
                            // iconUrl: "http://www.google.com/favicon.ico",
                            iconUrl: "images/icon.png",
							type: "basic",
							message: result.keywords
						};
						chrome.notifications.create('WikiNotif2', notifOptions);


                        console.log(result)
						
					});
		}
			
			
		$('#keyword').val('');
		
    });
});