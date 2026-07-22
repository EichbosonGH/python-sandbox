
# Alternativen zu pyinstaller

## Übersicht laut ChatGPT
| Tool                  | Status        | Einzelne EXE                   | Performance | Empfehlung                         |
| --------------------- | ------------- | ------------------------------ | ----------- | ---------------------------------- |
| **PyInstaller**       | Sehr aktiv    | ✅                              | Gut         | Standardlösung                     |
| **Nuitka**            | Sehr aktiv    | ✅                              | Sehr gut    | Beste Wahl für produktive Software |
| **cx_Freeze**         | Aktiv         | ⚠️ Eher Ordner als Single-File | Gut         | Gut für klassische Desktop-Apps    |
| **PyOxidizer**        | Weniger aktiv | ✅                              | Sehr gut    | Für Spezialfälle                   |
| **BeeWare Briefcase** | Aktiv         | ❌ (App-Paket)                  | Gut         | Für GUI-Anwendungen                |
| **Py2exe**            | Kaum relevant | Teilweise                      | Mittel      | Heute kaum noch empfehlenswert     |

## Nuitka

* Die derzeit beliebteste Alternative. Übersetzt deinen Python-Code tatsächlich zu C-Code und kompiliert diesen dann – dadurch oft schneller zur Laufzeit und schwerer zu "reverse engineeren" als PyInstaller (das nur Bytecode bündelt).

* Nachteil: Kompilieren dauert länger, braucht einen C-Compiler (unter Windows z. B. MSVC oder MinGW, wird bei Bedarf automatisch geholt).

~~~powershell
uv tool install nuitka
nuitka --onefile --output-filename=meinprogramm zufallszahl.py
~~~

## Andere

### cx_Freeze
- Ähnliches Prinzip wie PyInstaller (bündelt Interpreter + Bytecode), etwas älter, weniger "magisch" automatisiert – man muss oft mehr manuell in einer setup.py konfigurieren.

### py2exe
- Nur für Windows, sehr alt, wird kaum noch aktiv weiterentwickelt. Für neue Projekte nicht empfehlenswert.

### auto-py-to-exe
- Kein echter eigener Compiler, sondern eine grafische Oberfläche (GUI) für PyInstaller. Praktisch, wenn du die ganzen Kommandozeilen-Optionen nicht auswendig lernen willst.

### PyOxidizer
- Ambitioniertes Rust-basiertes Projekt, bettet einen Python-Interpreter direkt in ein Rust-Binary ein. Wird aber seit einiger Zeit kaum noch weiterentwickelt – eher nicht empfehlenswert für neue Projekte.




