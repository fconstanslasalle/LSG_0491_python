# 24-25-python-game-PauSGracia
24-25-python-game-PauSGracia created by GitHub Classroom

<p>El joc que vull desenvolupar es el Pong. </p>
<p>En la finestra hi haura 2 pales, 1 pilota i 2 textos que diran la puntuació de cada jugador.</p>
<p>La pala de l'esquerra es mourà amb W i S, mentres que la pala de la dreta es mourà amb la fletxa d'adalt i la fletxa d'abaix.</p>
<p>Les pales mai podràn sortir de la pantalla.</p>
<p>La pilota es mou sola.</p>
<p>La pilota s'inicia movent-se en una direcció aleatoria.</p>
<p>Cada vegada que la pilota toqui la part esquerra de la pantalla, el jugador de la dreta rebrà 1 punt.</p>
<p>Cada vegada que la pilota toqui la part dreta de la pantalla, el jugador de l'esquerra rebrà 1 punt.</p>
<p>Cada vegada que la pilota toqui la part d'adalt o la part d'abaix de la pantalla, la velocitat es multiplicarà per -1.</p>
<p>No hi ha limit de puntuació.</p>
<p>Al principi de la partida i cada vegada que un jugador faci un punt, hi ha un temporitzador per què els jugadors es pugiun preparar</p>

# Finestra
Així es com serà la finsetra del joc de pygame
![image](https://github.com/user-attachments/assets/295f9461-0582-4359-b820-6e9b7c7d027a)

# Striker
Amb la classe _Striker_ creada i amb el mètode _display_, podem mostrar una pala del pong. També és necesari posar el _pygame.display.update()_ _clock.tick(FPS)_ per actualitzar el joc constantment i que es pugui veure la pala.
![image](https://github.com/user-attachments/assets/06923169-866f-493e-a68e-30d1f2db7c34)

Creant una altre variable, podem afegir una segona pala:
![image](https://github.com/user-attachments/assets/155724fc-c8f6-4bf4-84cb-ba07cb1659d6)

Al afegir moviment, la pala es queda "enrere", no s'esborra la úlitma posició de la pala i no es pot verue bé a on està la pala actualment:
![image](https://github.com/user-attachments/assets/2fb60f7f-e120-4d4a-8a53-162bc19e719d)

Per arreglar aquest problema, he afegit _screen.fill((0,0,0))_ al principi del bucle del joc. D'aquesta manera pinto la pantalla de negre i despres les pales, eliminant el bug.

# Ball
Amb la classe _Ball_, tenim una pilota que es mou sola, detecta si colisiona amb les parets o amb algun jugador, si algú ha conseguit algun punt i quan ha de tornar a la posició inicial.
![image](https://github.com/user-attachments/assets/1ec131e0-47c8-4a1c-8dd3-f0a97f695b43)

# Score
Afegim a dalt de la finestra un text amb la puntuació de cada jugador.
![image](https://github.com/user-attachments/assets/10b09d80-2b5a-4d4f-83a2-4d6904206783)

# Timer
Posem un temporitzador al començament del joc i quan un jugador marca algun punt. Així, els jugadors tenent temps per preparar-se
![image](https://github.com/user-attachments/assets/ca595656-ba3c-458d-a2a3-39c6e2204e09)


