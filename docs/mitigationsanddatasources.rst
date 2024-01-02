Mitigations and Data Sources
=============================

The MITRE ATT&CK framework has mapped data sources and mitigations, where applicable, to each of the techniques detailed in the framework. These have been validated in terms of external actors, but the MITRE research team behind the Insider Threat Knowledge Base wanted to validate these for applicability to insider threats. We are working under the assumption that many or most of the mitigations and data sources listed will help both efforts, but that there will likely be some differences or additional data sources and mitigations.

Mitigations 
------------
Mitigations have been identified through their mappings to ATT&CK TTPs and through validation by Center participants. Currently all insider threat TTPs within the Knowledge Base are also TTPs in ATT&CK, therefore those identified mitigations have been considered. Through discussion with participants, further mitigations may be identified. 

.. raw:: html
   
   <iframe src="../_static/html/mitigations-1.html" height="845px" width="100%"></iframe>

Data Sources
-------------
Identifying the most common data sources to detect insider threat will enhance the communities ability to prevent further threats. The data sources will be identified first through mappings from ATT&CK, like the mitigations. However, Center participants have identified and confirmed the data sources used for each detected TTP. 

.. .. raw:: html
   
..    <iframe src="../_static/html/datasources-1.html" height="1045px" width="100%"></iframe>

.. raw:: html

   <div id="datasource-container">
      <iframe id="datasource" src="../_static/html/datasources-1.html" height="1045px" width="100%"></iframe>

      <button id="fullscreen-button" class="btn btn-secondary btn-sm" onclick="toggleFullscreen()">
               <i class="fa fa-arrows-alt"></i>
               Full Screen
         </button>
         
      <script>
         function toggleFullscreen() {
            if (document.fullscreenElement) {
                  document.exitFullscreen();
            } else {
                  document.querySelector("#datasource-container").requestFullscreen();
            }
         }
      </script>

      <style>
      #datasource-container {
         position: relative;
      }

      #fullscreen-button {
         position: absolute;
         bottom: 5px;
         right: 5px;
      }

      @media all and (display-mode: fullscreen) {
         #datasource-container {
            display: flex;
            align-items: center;
            justify-content: center;
         }

         #datasource {
            max-width: 80vw;
            max-height: 100vh;
         }
      }
      </style>

   </div>
   
.. .. raw:: html

..     <style>
..     #preview {
..         border: 1px solid black;
..         background-color: white;
..         height: 30rem;
..         position: relative;
..         overflow: scroll;
..     }

..     #preview button {
..         position: absolute;
..         bottom: 5px;
..         right: 5px;
..     }

..     #preview p {
..         color: #bebebe;
..         margin-top: 14em;
..         text-align: center;
..     }

..     #preview svg {
..         display: block;
..         width: 100%;
..         height: auto;
..     }

..     @media all and (display-mode: fullscreen) {
..         #preview svg {
..             max-width: 100vw;
..             max-height: 100vh;
..         }
..     }

..     #previewError {
..         color: var(--me-ext-cranberry-dark);
..         background-color: #f3bacf;
..         border: 1px solid var(--me-ext-cranberry-dark);
..         margin: 1em 0;
..         padding: 1em;
..         display: none;
..     }
..     </style>
..     <div id="preview">
..         <button class="btn btn-secondary btn-sm" onclick="toggleFullscreen()">
..             <i class="fa fa-arrows-alt"></i>
..             Full Screen
..         </button>
..         <p>
..             Preview: Select Full Screen for entire view.
..         </p>
..     </div>

..     <div style="display: flex; margin-top: 1em;">
..         <div style="flex-grow: 1;">
..             <label for="layerSelect">
..                 Select or upload base layer:
..             </label>
..             <select id="layerSelect" onchange="selectBaseLayer(this)">
..                 <option value=""></option>
..                 <option value="enterprise-subs-blank">Enterprise Techniques and Subtechniques</option>
..                 <option value="enterprise-mitigations-blank">Enterprise Techniques and Mitigations</option>
..                 <option value="enterprise-datasources-blank">Enterprise Techniques and Datasources</option>
..                 <option value="upload">Upload (.svg)</option>
..             </select>
..             <br>
..             <input id="baseLayerUpload" type="file" onchange="uploadBaseLayer(this)"
..                 accept=".svg" style="margin-top: 0.5em; visibility: hidden;">
..         </div>
..       </div>   

..       <div style="margin-bottom: 3em;">
..         <button class="btn btn-primary" onclick="generatePreview()">
..             <i class="fa fa-search"></i>
..             Generate Preview
..         </button>
..         <button id="downloadSvg" class="btn btn-primary" onclick="downloadSvg()" disabled>
..             <i class="fa fa-download"></i>
..             Download
..         </button>
..     </div>

..         <script src="../matrix/matrix.js"></script>

..     <script>
..     let layerSrc = null;
..     let flowSrc = null;
..     let svgSrc = null;

..     function selectBaseLayer(el) {
..         if (el.value === "upload") {
..             document.querySelector("#baseLayerUpload").click();
..         } else if (el.value !== "") {
..             const url = `../matrix/${el.value}.svg`;
..             fetch(url).then((response) => response.text())
..             .then((data) => {
..                 layerSrc = data;
..             })
..             .catch((err) => showError(`Cannot download base layer: ${url}`));
..         }
..     }

..     function uploadBaseLayer(fileInput) {
..         const fr = new FileReader();
..         fr.onload = () => layerSrc = fr.result;
..         fr.readAsText(fileInput.files[0]);
..     }

..     function uploadAttackFlow(fileInput) {
..         const fr = new FileReader();
..         fr.onload = () => flowSrc = fr.result;
..         fr.readAsText(fileInput.files[0]);
..     }

..     function toggleFullscreen() {
..         if (document.fullscreenElement) {
..             document.exitFullscreen();
..         } else {
..             document.querySelector("#preview").requestFullscreen();
..         }
..     }

..     function generatePreview() {
..         if (!layerSrc) {
..             showError("Select or upload a base layer before previewing.");
..             return;
..         }

..         if (!flowSrc) {
..             showError("Upload an Attack Flow (.json) before previewing.");
..             return;
..         }

..         try {
..             for (const el of document.querySelectorAll("#preview svg")) {
..                 el.remove();
..             }
..             svgSrc = render(layerSrc, flowSrc);
..             const container = document.createElement("div");
..             container.innerHTML = svgSrc;
..             const svg = container.querySelector("svg");
..             const svgWidth = svg.getAttribute("width");
..             const svgHeight = svg.getAttribute("height");
..             svg.setAttribute("viewBox", `0 0 ${svgWidth} ${svgHeight}`);
..             container.removeChild(svg);
..             document.querySelector("#preview").appendChild(svg);
..             document.querySelector("#preview p").style.display = "none";
..             document.querySelector("#downloadSvg").disabled = false;
..             hideError();
..         } catch (e) {
..             showError(`Cannot generate preview: ${e}`);
..             throw e;
..         }
..     }

..     function downloadSvg() {
..         const file = document.querySelector("#uploadFlow").files[0];
..         const fileName = file.name.replace(".json", ".svg");
..         let data = '<?xml version="1.0" standalone="no"?>\n';
..         data += svgSrc;
..         const blob = new Blob([data], {type:"image/svg+xml"});
..         const anchor = document.createElement("a");
..         anchor.download = fileName;
..         anchor.href = URL.createObjectURL(blob);
..         anchor.style.display = "none";
..         document.body.appendChild(anchor);
..         anchor.click();
..         setTimeout(function () {
..             document.body.removeChild(anchor);
..             URL.revokeObjectURL(anchor.href);
..         }, 500);
..     }

..     function showError(txt) {
..         const errorDiv = document.querySelector("#previewError");
..         const errorSpan = errorDiv.querySelector("span");
..         errorSpan.innerText = txt;
..         errorDiv.style.display = "block";
..     }

..     function hideError() {
..         document.querySelector("#previewError").style.display = "none";
..     }
..     </script>

