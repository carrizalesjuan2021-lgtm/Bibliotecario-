import json
from IPython.display import display, HTML, Javascript
from google.colab import output


knowledge_base = {
    "TICS": {

        "1er Semestre": {
            "Algebra Lineal": [
                {"title": "Álgebra Lineal 1", "author": "Stanley I. Grossman", "description": "Un clásico para entender los conceptos fundamentales de vectores, matrices y determinantes.", "keywords": ["vectores", "matrices", "determinantes"], "link": "https://example.com/algebra_grossman"},
                {"title": "Álgebra Lineal y sus Aplicaciones", "author": "David C. Lay", "description": "Ideal para una visión más aplicada y práctica de la materia.", "keywords": ["aplicaciones", "transformaciones", "ejercicios"], "link": "https://example.com/algebra_lay"}
            ]
        },

        "3er Semestre": {
            "Programación Orientada a Objetos": [
                {"title": "The Art of the B-Tree", "author": "D. E. Knuth", "description": "Libro técnico y avanzado sobre los fundamentos de las estructuras de datos tipo árbol.", "keywords": ["algoritmos", "estructuras de datos", "arboles"], "link": "https://example.com/btree_knuth"},
                {"title": "Introduction to Algorithms", "author": "T. H. Cormen", "description": "Libro base para la materia, el que todo programador debe tener.", "keywords": ["algoritmos", "fundamentos", "complejidad"], "link": "https://example.com/algorithms_cormen"},
                {"title": "Design Patterns: Elements of Reusable Object-Oriented Software", "author": "Gamma, Helm, Johnson, Vlissides", "description": "Referencia para los patrones de diseño más comunes en POO.", "keywords": ["patrones de diseño", "POO", "refactorizacion"], "link": "https://example.com/design_patterns"}
            ],
            "Cálculo Integral": [
                {"title": "Calculus, Volume II", "author": "Tom M. Apostol", "description": "Un texto formal y riguroso que cubre cálculo integral con fundamentos matemáticos profundos.", "keywords": ["cálculo integral", "riguroso", "universidad", "matemáticas avanzadas"], "link": "https://example.com/apostol_calc2"},
                {"title": "Calculus with Analytic Geometry", "author": "George B. Thomas, Ross L. Finney", "description": "Un libro clásico, accesible pero completo, ideal para cursos universitarios.", "keywords": ["cálculo", "integrales", "universitario", "geometría analítica"], "link": "https://example.com/thomas_calculus"},
                {"title": "Schaum's Outline of Calculus", "author": "Frank Ayres, Elliott Mendelson", "description": "Guía práctica con muchos ejercicios y explicaciones claras para reforzar conceptos de integral.", "keywords": ["ejercicios", "resumen", "integrales", "práctica"], "link": "https://example.com/schaum_calculus"},
                {"title": "Calculus: Early Transcendentals", "author": "James Stewart", "description": "Uno de los libros más usados en ingeniería; explica integrales con aplicaciones reales.", "keywords": ["ingeniería", "aplicaciones", "transcendentales", "integrales"], "link": "https://example.com/stewart_transcendentals"},
                {"title": "Elementary Calculus: An Infinitesimal Approach", "author": "H. Jerome Keisler", "description": "Explica cálculo usando infinitesimales, con un enfoque intuitivo y pedagógico.","keywords": ["infinitesimales", "intuitivo", "bases", "integrales"], "link": "https://example.com/keisler_calculus"}
            ],
        },

        "5to Semestre": {
            "Programación Web": [
                {"title": "HTML and CSS: Design and Build Websites", "author": "Jon Duckett", "description": "Excelente para principiantes en diseño web.", "keywords": ["html", "css", "principiantes", "diseño web"], "link": "https://example.com/html_css_duckett"},
                {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "description": "Una guía concisa para escribir JavaScript de calidad.", "keywords": ["javascript", "js", "frontend", "mejoras"], "link": "https://example.com/js_crockford"}
            ],
            "Redes de computadoras": [
                {"title": "Computer Networks", "author": "Andrew S. Tanenbaum; David J. Wetherall", "description": "Texto clásico y exhaustivo sobre redes de computadoras que explica modelos (OSI y TCP/IP), protocolos, conmutación y enrutamiento, enlace de datos, control de errores y fundamentos de seguridad. Muy recomendable para estudiantes y profesionales que buscan tanto teoría como aplicaciones prácticas.", "keywords": ["redes", "TCP/IP", "OSI", "enrutamiento", "protocolos", "Ethernet"], "link": "https://en.wikipedia.org/wiki/Computer_Networks_(book)"}
            ],
                {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "description": "Una guía concisa para escribir JavaScript de calidad.", "keywords": ["javascript", "js", "frontend", "mejoras"], "link": "https://example.com/js_crockford"},
                {"title": "HTML y CSS Facil", "author": "Arnaldo Perez Castano", "description": "Un libro conciso para aprender a escribir HTML y CSS de calidad, y de manera facil.", "keywords": ["html", "css", "frontend", "facil"], "link": "https://www.buscalibre.com.mx/libro-html-y-css-facil/9788426721853/p/46343925"}
                {"title": "Introducción a la programación web avanzada", "author": "Jordi Sánchez Cano", "description": "Una guía concisa para crear sitios web de calidad.", "keywords": ["vss", "html", "frontend", "mejoras"], "link": "https://dl.dropboxusercontent.com/scl/fi/935ne5q5fmjr5pecqikt9/introduccion-a-la-programacion-web-avanzada-jordi-sanchez-cano.pdf?rlkey=2kcdf34hl65aekp2hgwrabdvc&dl=0"}
            ]
        }
    },
}

def recommend_book(career, semester, subject, description):
    subjects = knowledge_base.get(career, {}).get(semester, {})
    books = subjects.get(subject, [])
    if not books: return None
    user_keywords = description.lower().split()
    max_score, best_book = -1, None
    for book in books:
        score = sum(1 for user_kw in user_keywords if user_kw in [kw.lower() for kw in book.get("keywords", [])])
        if score > max_score:
            max_score, best_book = score, book
    return best_book

# Función para manejar la solicitud de búsqueda desde JS
def handle_search_request(data_json):
    """Maneja la solicitud de búsqueda desde la interfaz de JavaScript."""
    try:
        data = json.loads(data_json)
        recommended_book = recommend_book(data.get('career'), data.get('semester'), data.get('subject'), data.get('description'))
        if recommended_book is None:
            result_message = "❌ No se encontró un libro recomendado para esta descripción."
            display(Javascript(f"""
                document.getElementById('search-result-area').className = 'result error';
                document.getElementById('search-result-area').innerHTML = `{result_message}`;
            """))
        else:
            result_message = f"📖 **Libro recomendado:** <a href='{recommended_book['link']}' target='_blank'>{recommended_book['title']}</a> de {recommended_book['author']}<br><span style='font-size: 0.9em; color: #666;'>{recommended_book['description']}</span>"
            display(Javascript(f"""
                document.getElementById('search-result-area').className = 'result success';
                document.getElementById('search-result-area').innerHTML = `{result_message}`;
            """))
    except json.JSONDecodeError:
        display(Javascript(f"""
            document.getElementById('search-result-area').className = 'result error';
            document.getElementById('search-result-area').innerHTML = 'Error al procesar la solicitud. Inténtalo de nuevo.';
        """))

# Registra la función de Python para que pueda ser llamada desde JavaScript
output.register_callback('handle_search_request_callback', handle_search_request)

# 2. INTERFAZ DE USUARIO CON HTML, CSS Y JAVASCRIPT
html_code = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    :root {{
        --primary-color: #4a90e2;
        --secondary-color: #50e3c2;
        --background-color: #f0f2f5;
        --card-bg-color: #ffffff;
        --text-color: #333;
        --soft-text-color: #888;
        --border-color: #e0e0e0;
    }}
    body {{ font-family: 'Poppins', sans-serif; background-color: var(--background-color); color: var(--text-color); line-height: 1.6; }}
    .container {{ max-width: 650px; margin: 40px auto; padding: 30px; background-color: var(--card-bg-color); border-radius: 15px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08); }}
    h2 {{ color: var(--primary-color); text-align: center; margin-bottom: 30px; font-weight: 600; letter-spacing: -0.5px; }}
    .form-group {{ margin-bottom: 25px; }}
    label {{ display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color); }}
    input, select, textarea {{ width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; box-sizing: border-box; font-size: 16px; transition: border-color 0.3s; }}
    input:focus, select:focus, textarea:focus {{ outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2); }}
    textarea {{ resize: vertical; height: 120px; }}
    .btn {{ width: 100%; padding: 15px; background-color: var(--primary-color); color: #fff; border: none; border-radius: 8px; font-size: 18px; font-weight: 600; cursor: pointer; transition: background-color 0.3s, transform 0.1s; }}
    .btn:hover {{ background-color: #387ad6; }}
    .btn:active {{ transform: scale(0.98); }}
    .search-btn {{ background-color: var(--secondary-color); color: var(--text-color); font-size: 16px; margin-top: 10px; margin-bottom: 20px; }}
    .search-btn:hover {{ background-color: #43c9aa; }}
    .result {{ margin-top: 25px; padding: 18px; border-radius: 10px; font-size: 15px; }}
    .success {{ background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }}
    .warning {{ background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }}
    .error {{ background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }}
    #welcome-view, #app-view {{ display: none; }}
</style>

<div class="container">
    <div id="welcome-view">
        <h2>📚 Buscador de Recursos</h2>
        <p>Encuentra el libro ideal para tu tarea. Comienza seleccionando tu carrera y semestre.</p>
        <button id="start-btn" class="btn">Comenzar</button>
    </div>
    <div id="app-view">
        <div id="task-form-view">
            <h2>Busca un Recurso</h2>
            <form id="taskForm">
                <div class="form-group"><label for="career">Carrera:</label><select id="career" required></select></div>
                <div class="form-group"><label for="semester">Semestre:</label><select id="semester" required></select></div>
                <div class="form-group"><label for="subject">Materia:</label><select id="subject" required></select></div>
                <div class="form-group">
                    <label for="description">Descripción de la tarea:</label>
                    <textarea id="description" placeholder="Ej. 'Estudiar sobre matrices y vectores para el examen'"></textarea>
                    <button type="button" id="search-book-btn" class="btn search-btn">Buscar Libro</button>
                </div>
                <div id="search-result-area" class="result"></div>
            </form>
        </div>
    </div>
</div>

<script>
    const knowledgeBase = """ + json.dumps(knowledge_base) + """;
    const careerSelect = document.getElementById('career');
    const semesterSelect = document.getElementById('semester');
    const subjectSelect = document.getElementById('subject');
    const searchBookBtn = document.getElementById('search-book-btn');
    const descriptionTextarea = document.getElementById('description');
    const searchResultArea = document.getElementById('search-result-area');
    const welcomeView = document.getElementById('welcome-view');
    const appView = document.getElementById('app-view');
    const startBtn = document.getElementById('start-btn');

    // Iniciar la aplicación
    welcomeView.style.display = 'block';
    appView.style.display = 'none';
    startBtn.onclick = () => {
        welcomeView.style.display = 'none';
        appView.style.display = 'block';
        updateCareers();
        updateSemesters();
        updateSubjects();
    };

    // Llenar el dropdown de carreras
    function updateCareers() {
        careerSelect.innerHTML = '<option value="">Selecciona una carrera...</option>';
        for (const career in knowledgeBase) {
            const option = document.createElement('option');
            option.value = career;
            option.textContent = career;
            careerSelect.appendChild(option);
        }
    }

    // Actualizar el dropdown de semestres
    function updateSemesters() {
        const selectedCareer = careerSelect.value;
        semesterSelect.innerHTML = '<option value="">Selecciona un semestre...</option>';
        if (selectedCareer && knowledgeBase[selectedCareer]) {
            for (const semester in knowledgeBase[selectedCareer]) {
                const option = document.createElement('option');
                option.value = semester;
                option.textContent = semester;
                semesterSelect.appendChild(option);
            }
        }
        updateSubjects();
    }
    careerSelect.addEventListener('change', updateSemesters);

    // Actualizar el dropdown de materias
    function updateSubjects() {
        const selectedCareer = careerSelect.value;
        const selectedSemester = semesterSelect.value;
        subjectSelect.innerHTML = '<option value="">Selecciona una materia...</option>';
        if (selectedCareer && selectedSemester && knowledgeBase[selectedCareer][selectedSemester]) {
            for (const subject in knowledgeBase[selectedCareer][selectedSemester]) {
                const option = document.createElement('option');
                option.value = subject;
                option.textContent = subject;
                subjectSelect.appendChild(option);
            }
        }
    }
    semesterSelect.addEventListener('change', updateSubjects);

    // Búsqueda de libro al hacer clic en el botón
    searchBookBtn.addEventListener('click', function(event) {
        event.preventDefault();
        const data = {
            career: careerSelect.value,
            semester: semesterSelect.value,
            subject: subjectSelect.value,
            description: descriptionTextarea.value
        };
        if (!data.career || !data.semester || !data.subject || !data.description) {
            searchResultArea.className = 'result error';
            searchResultArea.innerHTML = 'Por favor, completa todos los campos para buscar un libro.';
            return;
        }

        const data_json = JSON.stringify(data);

        // **MÉTODO CORREGIDO:** Llama a la función de Python a través de google.colab.kernel
        google.colab.kernel.invokeFunction('handle_search_request_callback', [data_json], {});

        searchResultArea.className = 'result warning';
        searchResultArea.innerHTML = 'Buscando libro...';
    });
</script>
"""
display(HTML(html_code))
