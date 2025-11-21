function getBhkvalue(){
    var ibhk=document.getElementsByName('uibhk');
    for(var i in ibhk){
       if(ibhk[i].checked){
            return parseInt(i)+1;
       }
    }
    return -1;
}
function getbathvalue(){
    var bath=document.getElementsByName('uibath');
    for(var i in bath){
        if(bath[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1;
}
function onClickedEstimatePrice(){
    var sqft=document.getElementById('area');
    var bhk=getBhkvalue();
    var bath=getbathvalue();
    var location=document.getElementById('uiLocations')
    var estPrice=document.getElementById('uiEstimatedPrice')

    var url='http://127.0.0.1:5000/predict_home_price'

    $.post(url,{
        total_sqft: parseInt(sqft.value),
        bhk: bhk,
        bath: bath,
        location: location.value
    },function(data,status){
        console.log(data.estimated_price);
        estPrice.innerHTML="<h2>"+data.estimated_price.toString()+" Lakh</h2>";
        console.log(status)
    });

}
function onPageLoad(){
    console.log('documnet loaded');
    var url='http://127.0.0.1:5000/get_location_names';
    $.get(url,function(data,status){
        console.log('get response for the get_name_locations');
        if(data){
            var locations=data.locations;
            var uiLocations=document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations){
                var opt=new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}
window.onload=onPageLoad();