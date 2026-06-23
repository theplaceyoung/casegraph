let graphData;
let cy;

fetch("/generated/graph.json")
.then(response => response.json())
.then(data => {

    graphData = data;

    cy = cytoscape({

        container: document.getElementById('cy'),

        elements: [
            ...data.nodes,
            ...data.edges
        ],

        userZoomingEnabled: true,
        userPanningEnabled: true,

        minZoom: 0.1,
        maxZoom: 5,

        wheelSensitivity: 0.2,

        style: [

            {
                selector: 'node',
                style: {

                    'label': '',

                    'width': 40,
                    'height': 40,

                    'background-color': '#3b82f6',

                    'font-size': '18px',

                    'text-wrap': 'wrap',
                    'text-max-width': '200px',

                    'text-valign': 'bottom',
                    'text-margin-y': 15,

                    'color': 'black'
                }
            },

            {
                selector: 'edge',
                style: {

                    'curve-style': 'bezier',

                    'target-arrow-shape': 'triangle',

                    'line-color': '#999',

                    'target-arrow-color': '#999'
                }
            }

        ],

        layout: {

            name: 'cose',

            animate: true

        }

    });


    // 노드 클릭
    cy.on('tap', 'node', function (evt) {

        const node = evt.target;

        document.getElementById("node-info").innerHTML = `

            <h2>${node.data('label')}</h2>

            <hr>

            <p><b>유형</b></p>
            <p>${node.data('type')}</p>

            <p><b>사건명</b></p>
            <p>${node.data('case_name') || ''}</p>

            <p><b>주문</b></p>
            <p>${node.data('order') || ''}</p>

            <p><b>이유</b></p>
            <p>${node.data('reason') || ''}</p>

            <p><b>기초사실</b></p>
            <p>${node.data('facts') || ''}</p>

            <p><b>결론</b></p>
            <p>${node.data('decision') || ''}</p>

        `;

    });


    // 빈 그래프
    if (data.nodes.length === 0) {

        document.getElementById("node-info").innerHTML = `

            <h3>CaseGraph</h3>

            <hr>

            PDF를 선택한 후<br><br>

            Generate CaseGraph를 눌러주세요.

        `;
    }

});


//
// Generate
//
document
.getElementById("generate-btn")
.addEventListener("click", () => {

    const fileInput =
        document.getElementById("pdf-file");

    if (fileInput.files.length === 0) {

        alert("PDF를 선택하세요.");

        return;
    }

    const formData = new FormData();

    formData.append(
        "pdf",
        fileInput.files[0]
    );

    fetch(
        "/upload",
        {
            method: "POST",
            body: formData
        }
    )
    .then(response => response.json())
    .then(data => {

        alert("CaseGraph 생성 완료!");

        location.reload();

    });

});


//
// Export
//
document
.getElementById("export-btn")
.addEventListener("click", () => {

    if (!graphData) {

        alert("내보낼 그래프가 없습니다.");

        return;
    }

    const jsonString =
        JSON.stringify(
            graphData,
            null,
            2
        );

    const blob = new Blob(
        [jsonString],
        {
            type: "application/json"
        }
    );

    const url =
        URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download =
        "casegraph_result.json";

    a.click();

    URL.revokeObjectURL(url);

});


//
// Clear
//
document
.getElementById("clear-btn")
.addEventListener("click", () => {

    fetch("/reset")
    .then(response => response.json())
    .then(data => {

        document.getElementById(
            "pdf-file"
        ).value = "";

        location.reload();

    });

});