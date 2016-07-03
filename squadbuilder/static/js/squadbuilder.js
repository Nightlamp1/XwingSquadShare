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
	$('#popover').popover();
	
});

$(document.body).on('click','[type=deletepilot]',function(){
	current_upgrades = $(this).parent().siblings('span').each(function(){
		console.log($(this).data('cost'));
		cost-=$(this).data('cost');
	});

	/*for (i=0; i<upgrades[this.id].length; i++){
		var upgradeCost = $("."+upgrades[this.id][i]+this.id).data("cost");
		if (upgradeCost != null){
			cost-=upgradeCost;
		}//Cost not being removed correctly for multiple upgrade ships
		
	}*/
	$(this).parent().parent().remove();
	cost-=pilotCost[this.id];
	updateCostDisplay(cost);	
});



$("button[type='pilotbutton']").click(function(){
	console.log(this);
	var htmlString = "<div id=" + this.id + "upgrades>";
	htmlString += generateUpgradeHtml(this.id,false,[]);
	htmlString+="</div><br>";

	$("#squad").append("<div class=pilot id=" + this.id + ' name=' + this.name +">" + '<img src="/static/img/Pilots/' + this.id + '.jpg" height=259px width=200px>' + 
						htmlString + "</div>");
						
	cost+=pilotCost[this.id];
	updateCostDisplay(cost);
	
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
	var upgradeId = $(this).attr('id');
	var upgradeType = upgradeId.replace(/[0-9]/g,"");
	var upgradeCost=0;
	
	if(selectedUpgrade=="None"){
		upgradeCost=$(this).closest('div').siblings("."+upgradeId+pilot).data("cost");
		if(upgradeCost == null){
			upgradeCost=0;
		}
		$(this).closest('div').siblings("."+upgradeId+pilot).remove();
		updateCostDisplay(cost-=upgradeCost);
		
	}
	else if($(this).closest('div').siblings("."+upgradeId+pilot).length==0){
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];
		$(this).closest('div').before('<span class=' + upgradeId + pilot + ' name=u' + upgradeCode + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$(this).closest('div').siblings("."+upgradeId+pilot).data("cost",upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
	}
	else{
		upgradeCost=$(this).closest('div').siblings("."+upgradeId+pilot).data("cost");
		updateCostDisplay(cost-=upgradeCost);
		$(this).closest('div').siblings("."+upgradeId+pilot).remove();
		
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];
		$(this).closest('div').before('<span class=' + upgradeId + pilot + ' name=u' + upgradeCode + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$(this).closest('div').siblings("."+upgradeId+pilot).data("cost", upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
	}
	
	if(bonusCheck(selectedUpgrade)){
		$("div#" + pilot + "upgrades").empty();
		htmlString=generateUpgradeHtml(pilot,true,['Torpedoes','Torpedoes']);
		$("div#" + pilot + "upgrades").html(htmlString);

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
	$("#expansion-selector").empty();
	for(i=1;i<=numOfExpansions;i++){
		var expansionId = parseInt($("#"+i+"select").attr("name"));
		var expansionQty = parseInt($("#"+i+"select option:selected").text());
		var expansionArray = [expansionId,expansionQty];
		//expansionQtyList+="[" + expansionId + ",";
		//expansionQtyList+=expansionQty+"] ";
		expansionQtyList.push(expansionArray);
		$("#expansion-selector").append("<input type='hidden' name='expansionCode' value="+expansionArray+">");
	}
	//$('input[name="expansionCode"]').val(expansionQtyList);
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

function countUpgrade(pilotUpgrades, upgrade) {
    var count = 0;
    for (var i = 0; i < pilotUpgrades.length; i++) {
        if (pilotUpgrades[i] === upgrade) {
            count++;
        }
    }
    return count;
}

function isRestriction(currentPilot,currentUpgrade){
	var restriction = upgrade_restrictions[currentUpgrade];
	var pilot = available_pilots[currentPilot];
	if (restriction === undefined){
		return false;
	}
	else{
		var type = restriction['type'].toLowerCase();
		if(type =='action'){
			return false;
		}
		else{
			if(pilot[type]!=restriction['restriction']){
				return true;
			}else{
				return false;
			}
		}
	}
}

function bonusCheck(currentUpgrade){
	var checker = upgrade_bonus[currentUpgrade];
	if (checker === undefined){
		return false;
	}
	else{
		return true;
	}	
}

function generateUpgradeHtml(pilot,isBonus,bonusArray){
	
	var htmlString = "<button id=" + pilot + " type='deletepilot' class='btn btn-danger'>Remove Pilot</button> <h4>Choose Upgrades:</h4>";
	console.log(pilot);
	var pilotUpgradeList = upgrades[pilot];
	if(isBonus){
		console.log("Thar be a bonus");
		for(i=0;i<bonusArray.length; i++){
			pilotUpgradeList.push(bonusArray[i]);
		}
	}
	for (i=0; i<pilotUpgradeList.length; i++){
		htmlString += ("<span class='dropup'>");
		multipleChecker = countUpgrade(upgrades[pilot],upgrades[pilot][i]);
		if(multipleChecker > 1){
			htmlString += ("<button type='button' class='btn btn-default dropdown-toggle' id=" + pilot + upgrades[pilot][i] + i + " data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ upgrades[pilot][i] + "</button>"+
			"<ul class='dropdown-menu' aria-labelledby='test'>");
		}
		else{
			htmlString += ("<button type='button' class='btn btn-default dropdown-toggle' id=" + pilot + upgrades[pilot][i] + " data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ upgrades[pilot][i] + "</button>"+
			"<ul class='dropdown-menu' aria-labelledby='test'>");
		}
		
		upgradeCardArray=Object.keys(upgradeCardList[pilotUpgradeList[i].replace(/\s/g,"")]);
		var selected=upgrades[pilot][i].replace(/\s/g,"");
		for (j=0; j<upgradeCardArray.length; j++){
			if(multipleChecker>1){
				var selected=upgrades[pilot][i].replace(/\s/g,"");
				selected+=i;
			}
			var restricted = isRestriction(pilot,upgradeCardArray[j]);
			if(!restricted){
				htmlString+= ("<li><a class='upgrade' id=" + selected + ">" + upgradeCardArray[j] + "</a></li>");
			}
			
			
		}
		htmlString+=("<li><a class='upgrade' id=" + selected + ">None</a></li></ul>"+"</span>");
	
	}
	
	return htmlString;
}