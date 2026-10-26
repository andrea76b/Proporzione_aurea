# CLAUDE.md — Linee Guida Architetturali e Scientifiche per PHI-LAB v2.0 (Modalità A)

## 1. Configurazione per Claude GitHub App (Modalità A — Senza API Key)
Questo repository è progettato per interagire con **Claude Code Web (`claude.ai/code`)** e l'app desktop di Claude tramite la **Claude GitHub App ufficiale (`https://github.com/apps/claude`)** usando direttamente l'abbonamento dell'utente (Pro/Max/Team), senza necessità di chiavi API a consumo.

## 2. Guardia Epistemologica ("Avvocato del Diavolo" & Anti-Mito)
Ogni modifica al codice o ai contenuti operata da Claude DEVE rispettare il principio scientifico del progetto:
$$\text{Proporzione Aurea} = \text{Modello Utile} + \text{Verifica Empirica} - \text{Mito Estetico}$$
- **Immagini e Sobel**: L'analisi dei punti focali deve avvenire sempre sul buffer pixel pulito (`cleanOffscreenCanvas`) prima di disegnare le griglie sovrapposte, confrontando sempre $\varphi$ ($1.618$) con la Regola dei Terzi ($1.500$) e il rapporto $\sqrt{2}$ ($1.414$).
- **Chimica e Cristallografia**: Distinguere i semplici rapporti di massa stechiometrici dalla vera geometria molecolare 3D icosaedrica (Fullerene $\text{C}_{60}$ con vertici $(0, \pm 1, \pm 3\varphi)$, Icosaedro Platonico $(0, \pm 1, \pm \varphi)$, catena magnetica $\text{CoNb}_2\text{O}_6$ con simmetria $E_8$).
- **Biologia e Fillotassi**: Includere sempre le eccezioni biologiche (Serie di Lucas $2,1,3,4,7,11,18$ con angolo $\approx 99.5^\circ$, pattern decussati a $90^\circ$ e distici a $180^\circ$) e la smentita biometrica del *Nautilus pompilius* (rapporto medio $1.31$, non $1.618$).
- **Musica, Religioni e Biomeccanica**: Applicare i 4 livelli probatori nell'analisi musicale, separare la teologia simbolica rinascimentale di Luca Pacioli (1509) dalle attribuzioni infondate su testi antichi, e rispettare i limiti articolari fisiologici ($35^\circ\text{–}65^\circ$) nella dissociazione toraco-pelvica del Tango.

## 3. Regole Tecniche sul Codice
1. **Gestione Memoria GPU WebGL**: Usare sempre `clearAndDisposeGroup(group)` che invoca `.dispose()` su `Geometry` e `Material` prima di rimuovere gli oggetti 3D.
2. **Precisione Numerica**: Usare `const PHI = (1 + Math.sqrt(5)) / 2;` e `const GOLDEN_ANGLE_DEG = 360 * (1 - 1 / PHI);`.
3. **Zero Dipendenze Backend**: L'app deve restare 100% compatibile con GitHub Pages.
