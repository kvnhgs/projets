// Gestionnaire pour changer les onglets
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
  // Configurer le mode par défaut
  var toggleButton = document.getElementById('toggleMode');
  var bodyClassList = document.body.classList;
  var currentMode = localStorage.getItem('mode');

  // Définir le mode clair ou foncé selon localStorage
  if (currentMode === 'dark') {
      bodyClassList.remove('light-mode');
      toggleButton.innerHTML = '<i class="fas fa-sun"></i> Light mode';
  } else {
      bodyClassList.add('light-mode');
      toggleButton.innerHTML = '<i class="fas fa-moon"></i> Black mode';
  }

  // Écouteur d'événements pour le bouton de basculement du mode
  toggleButton.addEventListener('click', function() {
      bodyClassList.toggle('light-mode');
      if (bodyClassList.contains('light-mode')) {
          localStorage.setItem('mode', 'light');
          this.innerHTML = '<i class="fas fa-moon"></i> Black mode';
      } else {
          localStorage.setItem('mode', 'dark');
          this.innerHTML = '<i class="fas fa-sun"></i> Light mode';
      }
  });

  // Configurer les onglets
  var tablinks = document.getElementsByClassName('tablinks');
  for (var i = 0; i < tablinks.length; i++) {
      tablinks[i].addEventListener('click', function(event) {
          openTab(event, this.getAttribute('data-tab'));
      });
  }

  // Ouvrir l'onglet par défaut
  var defaultTab = document.getElementById('defaultOpen');
  if (defaultTab) {
      defaultTab.click();
  }
});
