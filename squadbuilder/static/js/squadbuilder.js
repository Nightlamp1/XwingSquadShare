var cost = 0;

//The following variables are defined in builder.html based on query data from views.py
//var upgrades = {{ upgrades|safe }}; A dict of {pilot:upgradeArray}
//var pilotCost = {{pilotCost|safe}}; A dict of {pilot:cost}
//var upgradeCardList = {{cards|safe}}; A dict of Upgrade card/cost sorted by type


$(document).ready(function() {
// Put all your setup procedures here, this is sort of like your 'constructor' 
//  for initializing variables and finalizing the page after the client has 
//	finished loading.
	$("#cost").text(cost +"/100");
	
});

$(".pilotCheckbox").change(function() {
  // Attach an event to all objects with class pilotCheckbox change events
  if(this.checked) {
	console.log(this.id);
	var htmlString = "<div id=" + this.id + "upgrades><h4>Choose Upgrades:</h4>";
	
	for (i=0; i<upgrades[this.id].length; i++){
		htmlString += (
		"<span class='dropdown'>"+
			"<button type='button' class='btn btn-default dropdown-toggle' id='test' data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ upgrades[this.id][i] + "</button>"+
			"<ul class='dropdown-menu' aria-labelledby='test'>");
	
		upgradeCardArray=Object.keys(upgradeCardList[upgrades[this.id][i]]);
		for (j=0; j<upgradeCardArray.length; j++){
			htmlString+= ("<li><a class='upgrade' id=" + upgrades[this.id][i] + ">" + upgradeCardArray[j] + "</a></li>");
			
		}
		htmlString+=("<li><a class='upgrade' id=" + upgrades[this.id][i] + ">None</a></li></ul>"+"</span>");
	
	}
	htmlString+="</div><br>"
	$("#squad").append("<div class=pilot id=" + this.id + ' name=' + this.name +">" + '<img src="/static/img/Pilots/' + this.id + '.jpg" height=259px width=200px>' + htmlString + "</div>");
	cost+=pilotCost[this.id];
	updateCostDisplay(cost);
	

  } else {
	for (i=0; i<upgrades[this.id].length; i++){
		var upgradeCost = $("."+upgrades[this.id][i]+this.id).data("cost");
		if (upgradeCost != null){
			cost-=upgradeCost;
		}
		
	}
	$("div#" +this.id).last().remove();
	cost-=pilotCost[this.id];
	updateCostDisplay(cost);
  }
});

$("#mytabs").click(function (e){
	$("input:checkbox").prop('checked', false);
	$("#squad").empty();
	cost = 0;
	updateCostDisplay(cost);
});



$(document.body).on('click','.upgrade',function(){
	
	var selectedUpgrade=$(this).text().replace(/\s/g,"");
	var pilot=$(this).closest('div').parent().attr('id');
	var upgradeType = $(this).attr('id');
	var upgradeCost=0;
	
	if(selectedUpgrade=="None"){
		upgradeCost=$("."+upgradeType+pilot).data("cost");
		if(upgradeCost == null){
			upgradeCost=0;
		}
		$("."+upgradeType+pilot).remove();
		updateCostDisplay(cost-=upgradeCost);
		
	}
	else if($("."+upgradeType+pilot).length==0){
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];
		console.log(pilot);
		$("div#"+pilot+"upgrades").before('<span class=' + upgradeType + pilot + ' name=u' + upgradeCode + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$("."+upgradeType+pilot).data("cost", upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
	}
	else{
		upgradeCost=$("."+upgradeType+pilot).data("cost");
		updateCostDisplay(cost-=upgradeCost);
		$("."+upgradeType+pilot).remove();
		
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];
		$("div#"+pilot+"upgrades").before('<span class=' + upgradeType + pilot + ' name=u' + upgradeCode + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$("."+upgradeType+pilot).data("cost", upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
	}
});

function updateCostDisplay(newvalue){
	if(newvalue <= 100){
		$("#cost").css('color','white');
		$("#cost").text(newvalue+"/100");
	}
	else{
		$("#cost").css('color','red');
		$("#cost").text(newvalue+"/100");
	}
}

//Currently function requires correct auto increment of mysqldb any skips in incrementation will break this logic
$('select').on('change',function(){
	var numOfExpansions = $(".expansion-qty").length;
	var expansionQtyList = [];
	for(i=1;i<=numOfExpansions;i++){
		expansionQtyList+=$("#"+i+"select option:selected").text();
	}
	$('input[name="expansionCode"]').val(expansionQtyList);
});

$('#savesquad').click(function(){
	if(cost > 100){
		$('#savedialog').html("<p> Squad value over 100. Please edit squad to less than or equal to 100 points </p>");
	}
	else{
		$('#savedialog').html("<input type='hidden' name='squadcode' value=''>"+
								"<br><h4>Enter Squad Name:</h4>"+
								"<input type='hidden' name='cost' value=''>"+
								"<input type='text' class='form-control' name='squadname' placeholder='Squad Name' aria-describedby='basic-addon1'><br>"+
								"<center><button id='finalsave' type='submit' class='btn btn-success'>Save Squad</button></center>");
		var numOfPilots = $(".pilot").length;
		var squadcode = "";
		$(".pilot").each(function(){
			squadcode+=$(this).attr('name');
			$(this).children("span").each(function(){
				if($(this).attr('class')!='dropdown'){
					squadcode+=$(this).attr('name');
				}
			});
		});
		$('input[name="squadcode"]').val(squadcode);
		$('input[name="cost"]').val(cost);
	}
});

function upvoteSquad(squadId,name){
	var token = getCookie('csrftoken');
	$.post("",{squadId : squadId, csrfmiddlewaretoken : token},function(data){
		console.log("post worked " + data);
		$('span[name='+name+']').each(function(){
			$(this).text(" " + data);
		});
	});
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
}