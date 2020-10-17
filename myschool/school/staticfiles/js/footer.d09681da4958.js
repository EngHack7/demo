function DateF() {
    var d = new Date();
var n = d.getFullYear();
console.log(n)
document.getElementById("footer-year").innerHTML = n.toString() + ' ' + 'work by';
}