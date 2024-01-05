function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
  
    // Cacher tous les contenus des onglets
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Enlever la classe 'active' de tous les onglets
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].classList.remove("active");
    }
  
    // Afficher le contenu de l'onglet actuel et ajouter la classe 'active'
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classList.add("active");
  }
  
  document.addEventListener("DOMContentLoaded", function() {
    // Ajouter des écouteurs d'événements pour chaque onglet
    var tablinks = document.getElementsByClassName("tablinks");
    for (var i = 0; i < tablinks.length; i++) {
      tablinks[i].addEventListener("click", function(event) {
        openTab(event, this.getAttribute("data-tab"));
      });
    }
  
    // Ouvrir l'onglet par défaut
    var defaultTab = document.getElementById("defaultOpen");
    if (defaultTab) {
      defaultTab.click();
    }
  });
  
  document.querySelectorAll('.dynamicButton').forEach(function(button) {
    button.addEventListener('click', function() {
        // La ligne suivante déclenche une boîte d'alerte, nous allons donc la commenter.
        // alert('Bouton ' + this.textContent + ' cliqué!');
    });
});

document.getElementById('toggleMode').addEventListener('click', function() {
  var icon = this.querySelector('i');
  
  document.body.classList.toggle('light-mode');
  
  if(document.body.classList.contains('light-mode')){
      this.innerHTML = '<i class="fas fa-moon"></i> Black mode'; // Change l'icône en lune
  } else {
      this.innerHTML = '<i class="fas fa-sun"></i> Light mode'; // Change l'icône en soleil
  }
});

