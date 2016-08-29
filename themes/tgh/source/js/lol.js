var pList = document.getElementsByClassName("project-list-container")[0];
var numProjects = pList.childNodes.length;

function appendProjects() {
  if ((window.innerHeight + window.scrollY + 150) > document.body.offsetHeight) {
    for(var i=0; i<numProjects; i++) {
      pList.appendChild(pList.childNodes[i].cloneNode(true));
    }
  }
}

window.onscroll = appendProjects;
appendProjects();
