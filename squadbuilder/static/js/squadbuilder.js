var cost = 0;

//The following variables are defined in builder.html based on query data from views.py
//var upgrades = {{ upgrades|safe }}; A dict of {pilot:upgradeArray}
//var pilotCost = {{pilotCost|safe}}; A dict of {pilot:cost}
//var upgradeCardList = {{cards|safe}}; A dict of Upgrade card/cost sorted by type
//var available_ships = {{available_ships|safe}}; A dict of available ships/quantities
//var available_pilots = {{available_pilots|safe}}; A dict of available pilots/quantities
//var upgrade_restrictions = {{upgrade_restrictions|safe}}; A dict of misc upgrade restrictions
//var upgrade_bonus = {{upgrade_bonus|safe}}; A dict of misc upgrade bonuses

$(document).ready(function() {
	//Initialize cost display
	$("#cost").text(cost +"/100");
	
});

$(document.body).on('click','[type=deletepilot]',function(){
	//Find each upgrade currently equiped and subtract it's cost from the total cost
	current_upgrades = $(this).parent().siblings('span').each(function(){
		var removeEval = $(this).children("img").attr('name');
		var current_pilot = $(this).parent().attr('id');
		var reg = new RegExp(current_pilot, "g");
		var upgrade_type = $(this).attr('class').replace(reg,"");
		updateUpgradeQty(removeEval,upgrade_type,true);
		cost-=$(this).data('cost');
	});
	//Remove the pilot html objects and subtract pilot cost from total cost
	//$(this).parent().parent().remove();
	cost-=pilotCost[this.id];
	updateCostDisplay(cost);
	//Increment the available_pilots qty by 1 for pilot being removed
	//Add pilot html selection button if it was previously removed
	available_pilots[this.id]['quantity']+=1;
	if(available_pilots[this.id]['quantity']==1){
		var code = available_pilots[this.id]['code'];
		var name = available_pilots[this.id]['name'];
		var pCost = available_pilots[this.id]['cost'];
		$("label#" + this.id).html("<button type='pilotbutton' class='btn btn-default' id=" + this.id + " name=p"+code +">"+
									"<span class='glyphicon glyphicon-plus' aria-hidden='true'></span>" + name + "-" + pCost + "</button>");
	}
	//Remove pilot html object
	$(this).parent().parent().remove();
});



$(document.body).on('click','[type=pilotbutton]',function(){
	//Generate upgrade html lists for selected pilot
	var htmlString = "<div id=" + this.id + "upgrades>";
	htmlString += generateUpgradeHtml(this.id,false,[]);
	htmlString+="</div><br>";
	//Add pilot object to squad viewer
	$("#squad").append("<div class=pilot id=" + this.id + ' name=' + this.name +">" + 
						'<img src="/static/img/Pilots/' + this.id + '.jpg" height=259px width=200px>' + 
						htmlString + "</div>");
	
	//Decrement available_pilot qty by 1 for pilot being added
	//Remove select pilot button if available_pilot qty is 0
	available_pilots[this.id]['quantity']-=1;
	if(available_pilots[this.id]['quantity']==0){
		$("label#"+this.id).empty();
	}
	//Increase squad cost and update cost display
	cost+=pilotCost[this.id];
	updateCostDisplay(cost);	
});

$("#mytabs").click(function (e){
	$("input:checkbox").prop('checked', false);
	$("div.pilot").each(function(){
		var pilot = $(this).attr('id');
		available_pilots[pilot]['quantity']+=1;
		var code = available_pilots[pilot]['code'];
		var name = available_pilots[pilot]['name'];
		var pCost = available_pilots[pilot]['cost'];
		$("label#" + this.id).html("<button type='pilotbutton' class='btn btn-default' id=" + this.id + " name=p"+code +">"+
									"<span class='glyphicon glyphicon-plus' aria-hidden='true'></span>" + name + "-" + pCost + "</button>");
	});
	$("img.upgrade").each(function(){
		var pilot = $(this).parent().parent().attr('id');
		var reg = new RegExp(pilot, "g");
		var upgrade_type = ($(this).parent().attr('class')).replace(reg,"");
		upgrade_type = upgrade_type.replace(/[0-9]/g,"");
		var upgrade = $(this).attr('name').replace(/--/g," ");
		updateUpgradeQty(upgrade,upgrade_type,true);
	});
	$("#squad").empty();
	cost = 0;
	updateCostDisplay(cost);
});



$(document.body).on('click','.upgrade',function(){
	
	var selectedUpgrade=$(this).text().replace(/\s/g,"");
	var upgradeEval=$(this).text().replace(/\s/g,"--");
	var pilot=$(this).closest('div').parent().attr('id');
	var upgradeId = $(this).attr('id');
	var upgradeType = upgradeId.replace(/[0-9]/g,"");
	var upgradeCost=0;
	var removeEval = "";
	var isRemoving = false;
	
	if(selectedUpgrade=="None"){
		isRemoving = true;
		upgradeCost=$(this).closest('div').siblings("."+upgradeId+pilot).data("cost");
		if(upgradeCost == null){
			upgradeCost=0;
		}
		removeEval = $(this).closest('div').siblings("."+upgradeId+pilot).children("img").attr('name');
		updateUpgradeQty(removeEval,upgradeId,true);
		$(this).closest('div').siblings("."+upgradeId+pilot).remove();
		updateCostDisplay(cost-=upgradeCost);	
	}
	else if($(this).closest('div').siblings("."+upgradeId+pilot).length==0){
		isRemoving = false;
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];

		$(this).closest('div').before('<span class=' + upgradeId + pilot + ' name=u' + upgradeCode + '> '+
									  '<img class="upgrade" name=' + upgradeEval + ' id=' + selectedUpgrade +
									  ' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$(this).closest('div').siblings("."+upgradeId+pilot).data("cost",upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
		updateUpgradeQty(upgradeEval,upgradeId,false);
	}
	else{
		isRemoving = true;
		upgradeCost=$(this).closest('div').siblings("."+upgradeId+pilot).data("cost");
		updateCostDisplay(cost-=upgradeCost);
		removeEval = $(this).closest('div').siblings("."+upgradeId+pilot).children("img").attr('name');
		updateUpgradeQty(removeEval,upgradeId,true);
		$(this).closest('div').siblings("."+upgradeId+pilot).remove();
		isRemoving = false;
		upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
		upgradeCode=upgradeCardList[upgradeType][$(this).text()]['code'];
		$(this).closest('div').before('<span class=' + upgradeId + pilot + ' name=u' + upgradeCode + '> ' + 
									  '<img class="upgrade" name=' + upgradeEval + ' id=' + selectedUpgrade +
									  ' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
		$(this).closest('div').siblings("."+upgradeId+pilot).data("cost", upgradeCost);
		updateCostDisplay(cost+=upgradeCost);
		updateUpgradeQty(upgradeEval,upgradeId,false);
	}
	
	
	domObject = $(this).closest('div');
	if(bonusCheck(upgradeEval) || bonusCheck(removeEval)){
		upgradeEval = upgradeEval.replace(/--/g," ");
		$("div#" + pilot + "upgrades").empty();
		if(isRemoving){
			removeEval = removeEval.replace(/--/g," ");
			for(i=0; i<upgrade_bonus[removeEval]['bonus'].length;i++){
				var bonusId = upgrade_bonus[removeEval]['bonus'][i];//May need to add indexing here
				upgradeCost=domObject.siblings("."+bonusId+pilot).data("cost");
				if(typeof upgradeCost !== "undefined"){
					updateCostDisplay(cost-=upgradeCost);
					upgradeToDelete = domObject.siblings("."+bonusId+pilot).children("img").attr('name').replace(/--/g," ");
					updateUpgradeQty(upgradeToDelete,bonusId,true);
					domObject.siblings("."+bonusId+pilot).remove();
				}	
			}
			htmlString=generateUpgradeHtml(pilot,false,[]);
		}else{
			htmlString=generateUpgradeHtml(pilot,true,upgrade_bonus[upgradeEval]['bonus']);	
		}
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

$('select').on('change',function(){
	var numOfExpansions = $(".expansion-qty").length;
	var expansionQtyList = [];
	$("#expansion-selector").empty();
	for(i=1;i<=numOfExpansions;i++){
		var expansionId = parseInt($("#"+i+"select").attr("name"));
		var expansionQty = parseInt($("#"+i+"select option:selected").text());
		var expansionArray = [expansionId,expansionQty];
		expansionQtyList.push(expansionArray);
		$("#expansion-selector").append("<input type='hidden' name='expansionCode' value="+expansionArray+">");
	}
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
	currentUpgrade = currentUpgrade.replace(/--/g," ");
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
	var pilotUpgradeList = [];
	for(i=0;i<upgrades[pilot].length;i++){
		pilotUpgradeList.push(upgrades[pilot][i]);
	}
	if(isBonus){
		
		for(i=0;i<bonusArray.length; i++){
			if(bonusArray[i][1]=="remove"){
				console.log("this will be removed");
				console.log(pilotUpgradeList);
				var upgrade_index = pilotUpgradeList.indexOf(bonusArray[i][0]);
				if (upgrade_index >= 0){
					pilotUpgradeList.splice(upgrade_index,1);
					console.log(pilotUpgradeList);
				}
			}
			else{
				pilotUpgradeList.push(bonusArray[i][0]);	
			}
			//bonusArray[i][0] will be the bonus, bonusArray[i][1] will be the type
		}
	}
	for (i=0; i<pilotUpgradeList.length; i++){
		htmlString += ("<span class='dropup'>");
		multipleChecker = countUpgrade(pilotUpgradeList,pilotUpgradeList[i]);
		if(multipleChecker > 1){
			htmlString += ("<button type='button' class='btn btn-default dropdown-toggle' id=" + pilot + pilotUpgradeList[i] + i +
						   " data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ pilotUpgradeList[i] + "</button>"+
						   "<ul class='dropdown-menu' type="+ pilotUpgradeList[i] + i + " aria-labelledby='test'>");
		}
		else{
			htmlString += ("<button type='button' class='btn btn-default dropdown-toggle' id=" + pilot + pilotUpgradeList[i] + 
						   " data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ pilotUpgradeList[i] + "</button>"+
						   "<ul class='dropdown-menu' type="+ pilotUpgradeList[i] +" aria-labelledby='test'>");
		}
		
		upgradeCardArray=Object.keys(upgradeCardList[pilotUpgradeList[i].replace(/\s/g,"")]);
		var selected=pilotUpgradeList[i].replace(/\s/g,"");
		for (j=0; j<upgradeCardArray.length; j++){
			if(multipleChecker>1){
				var selected=pilotUpgradeList[i].replace(/\s/g,"");
				selected+=i;
			}
			var restricted = isRestriction(pilot,upgradeCardArray[j]);
			if(!restricted){
				if(upgradeCardList[pilotUpgradeList[i].replace(/\s/g,"")][upgradeCardArray[j]]['quantity']>0){
					htmlString+= ("<li id="+upgradeCardArray[j].replace(/\s/g,"--")+ "><a class='upgrade' id=" + selected + ">" + upgradeCardArray[j] + "</a></li>");
				}
			}	
		}
		htmlString+=("<li><a class='upgrade' id=" + selected + ">None</a></li></ul>"+"</span>");
	}
	return htmlString;
}

function updateUpgradeQty(upgrade,type,isRemove){
	upgradeConverted=upgrade.replace(/\--/g," ");
	var typeHtmlId = type;
	var typeCleaned = type.replace(/[0-9]/g,"");
	if(isRemove){
		upgradeCardList[typeCleaned][upgradeConverted]['quantity']+=1;
		if(upgradeCardList[typeCleaned][upgradeConverted]['quantity']==1){
			$("li#"+upgrade).each(function(){
				typeHtmlId=$(this).parent().attr('type');
				$(this).html("<a class='upgrade' id=" + typeHtmlId + ">" + upgradeConverted + "</a>");
			});
		}
	}else{
		upgradeCardList[typeCleaned][upgradeConverted]['quantity']-=1;
		if(upgradeCardList[typeCleaned][upgradeConverted]['quantity']==0){
			$("li#"+upgrade).empty();
		}
	}	
}