const fileInput = document.getElementById('fileInput');
const imageDisplay = document.getElementById('imageDisplay');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const filePath = URL.createObjectURL(file);
        imageDisplay.src = filePath;
    }
});
const imgElement = document.createElement('img');
imgElement.src = 'path/to/image.jpg';
document.body.appendChild(imgElement);
const dropArea = document.getElementById('drop-area');

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file.type.startsWith('image/')) {
        const img = document.createElement('img');
        img.src = URL.createObjectURL(file);
        dropArea.appendChild(img);
    }
});
const { dialog, BrowserWindow } = require('electron');
const sharp = require('sharp');
const fs = require('fs');

function resizeImage(inputPath, outputPath, width, height, format = 'jpeg') {
    sharp(inputPath)
        .resize(width, height)
        .toFormat(format)
        .toFile(outputPath, (err, info) => {
            if (err) {
                console.error('Error resizing image:', err);
                return;
            }
            console.log('Image resized:', info);
        });
}

function openImageViewer(imagePath) {
    const imageWindow = new BrowserWindow({
        width: 800,
        height: 600,
    });

    imageWindow.loadURL(`file://${__dirname}/imageViewer.html?image=${imagePath}`);
}

function promptResizeDimensions() {
    return new Promise((resolve) => {
        dialog.showMessageBox({
            type: 'question',
            buttons: ['OK'],
            title: 'Resize Dimensions',
            message: 'Enter width and height (e.g., 500x300):',
            input: true,
        }).then((result) => {
            const dimensions = result.response.split('x');
            resolve({
                width: parseInt(dimensions[0], 10),
                height: parseInt(dimensions[1], 10),
            });
        });
    });
}

// Example usage
dialog.showOpenDialog({ properties: ['openFile', 'multiSelections'] }).then(async (result) => {
    if (!result.canceled) {
        const files = result.filePaths;
        const { width, height } = await promptResizeDimensions();

        files.forEach((file, index) => {
            const outputPath = `resized-output-${index + 1}.jpg`;
            resizeImage(file, outputPath, width, height);
            openImageViewer(outputPath);
        });
    }
});
document.getElementById('myButton').addEventListener('click', () => {
    alert('Button clicked!');
});