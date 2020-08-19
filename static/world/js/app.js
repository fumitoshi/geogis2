var mymap=L.map('map').setView([35.40, 136], 5);

var map1=L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png');///地理院
var map2=L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/english/{z}/{x}/{y}.png');///英語
var map3=L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/vbmd_bm/{z}/{x}/{y}.png');///火山

baseMaps={
  '日本語':map1,
  '英語':map2,
  '火山':map3,
}

L.control.layers(baseMaps).addTo(mymap);
map1.addTo(mymap);



/*
document.getElementById("checkbox").onclick=function(){
  $.getJSON("/world/geojson/",function(data){
    L.geoJson(data).addTo(mymap);
  });
};
*/
/*
function check(){
  $.getJSON("/world/geojson/",function(data){
    L.geoJson(data.location).addTo(mymap)
  });
};
*/


$.getJSON("/world/geojson/",function(data){
  L.geoJson(data).addTo(mymap);
});



/*
if(document.getElementById("chekbox").checked){
  function(){
    $.getJSON("/world/geojson/",function(data){
      L.geoJson(data).addTo(mymap);
    });
  };
}else{
{
    $.getJSON("",function(data){
      L.geoJson(data).addTo(mymap);
    });
  };
}
*/