# Project - Semester 5: Develop a math application

**Useful Links**
Cheat Sheet for GitHub/Git commands: https://education.github.com/git-cheat-sheet-education.pdf
Cheat Sheet for Markdown: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

**Short Git and GitHub Erklärung**

*GitHub*
1. Erstellt euch einen GitHub Account und schreibt euren Benutzernamen/Email in die WhatsApp Gruppe, so dass ich euch als Kollaboratoren zum Projekt hinzufügen kann!


*Git* 
1. Ladet euch Git https://git-scm.com/downloads herunter.
2. Fügt das Repository - was übrigen nur verwaltetes Verzeichnis bedeutet - als Remote Repository hinzu.
Da ich bisher die Repositories immer selbst erstellt habe, kann es sein, dass das nicht genau so funktioniert, wie ich das im folgenden beschreibe:
  1) Erstellt einen Ordner, der die Wurzel eures Repositories darstellen soll.
  2) Nun baut ihr eine Verbindung zum Remote Repository auf. Dazu nutzt ihr den Befehl "git remote add https://github.com/   RingTuEnigma/pyproject.git"
  3) Anschließend kopiert ihr euch alle Dateien aus dem GitHub Repository mit dem Befehl "git pull origin master".
  3) Mit dem Befehl "git add ." fügt ihr alle Dateien dem "Staging Prozess" hinzu. Alle bis zu diesem Zeitpunkt gemachten    Änderungen an den Dateien werden beim nächsten Commit als Version gespeichert. (Ihr müsst also jedes Mal "git add . /   filename" ausführen, wenn ihr von eurem aktuellen Dateistand eine Version wollt!)
  4) Nun führt ihr mit "git commit -m 'Initial commit' einen Commit aus. (Dies ist nur lokal und hat keinen Einfluss auf     das gemeinsame Remote Repository)
  5) Nun baut ihr die Verbindung zum Remote Repository auf, sodass ihr eure Änderungen dort speichern könnt. Dazu gebt       ihr den Befehl "git push" ein!
  
  !!Git push und Git pull funktionieren wahrscheinlich nicht so einfach, wenn mehrere in eine Branch pushen, dazu muss ich mich noch genauer informieren!!

