# Vehicle Damage Detection

A deep learning application that detects and classifies vehicle damage using computer vision. Built with PyTorch and Streamlit for easy web-based interaction.

## 🚗 Features

- **Real-time Damage Detection**: Upload vehicle images and get instant damage classification
- **6-Class Classification**: Detects Front/Rear damage with categories:
  - Front Breakage
  - Front Crushed
  - Front Normal
  - Rear Breakage
  - Rear Crushed
  - Rear Normal
- **Web Interface**: User-friendly Streamlit interface
- **Pre-trained Model**: Uses ResNet-50 architecture with transfer learning

## 📁 Project Structure

```
vehicle-damage-detection/
├── app.py                    # Streamlit web application
├── model_helper.py          # Model loading and prediction utilities
├── damage_prediction.ipynb  # Training notebook
├── requirements.txt         # Python dependencies
├── model/
│   └── resnet_model.pth     # Trained model weights
└── README.md               # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd vehicle-damage-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure model file exists**
   - Place your trained model file at `model/resnet_model.pth`
   - If you don't have a trained model, run the training notebook first

## 🚀 Usage

### Running the Web Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in the terminal

3. **Use the application**
   - Upload an image using the file uploader
   - Supported formats: JPG, JPEG, PNG
   - Click "Detect Damage" to analyze
   - View results and predictions

### Training Your Own Model

1. **Open the training notebook**
   ```bash
   jupyter notebook damage_prediction.ipynb
   ```

2. **Prepare your dataset**
   - Organize images in folders by class
   - Follow the 6-class structure mentioned above

3. **Run training cells**
   - Execute cells to train the ResNet-50 model
   - Model will be saved to `model/resnet_model.pth`

## 🧠 Model Architecture

- **Base Model**: ResNet-50 (pre-trained on ImageNet)
- **Transfer Learning**: 
  - Frozen early layers for feature extraction
  - Unfrozen layer4 for fine-tuning
  - Custom fully connected layer with dropout
- **Input Size**: 224x224 RGB images
- **Output**: 6-class classification

## 📋 Dependencies

```
streamlit==1.41.1
pillow==11.2.1
torch==2.7.0
torchvision==0.22.0
```

## 🎯 Model Performance

The model classifies vehicle damage into 6 categories:
- **Front damage**: Breakage, Crushed, Normal
- **Rear damage**: Breakage, Crushed, Normal

*Note: Add specific performance metrics after training evaluation*

## 📸 Example Usage

1. Upload a clear image of a vehicle (front or rear view)
2. Click "Detect Damage" button
3. View the predicted damage category
4. Results appear with confidence and classification

## 🔧 Troubleshooting

### Common Issues

**ModuleNotFoundError**: 
```bash
pip install -r requirements.txt
```

**Model file not found**:
- Ensure `model/resnet_model.pth` exists
- Run training notebook to generate the model

**Image processing errors**:
- Check image format (JPG, JPEG, PNG only)
- Ensure image is not corrupted
- Try reducing image size if too large

**Memory issues**:
- Use CPU version of PyTorch for lower memory usage
- Reduce batch size in training

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PyTorch team for the deep learning framework
- Streamlit for the web application framework
- ResNet authors for the model architecture
- ImageNet dataset for pre-trained weights

## 📞 Contact

For any inquiries, feel free to reach out:

**LinkedIN**: https://linkedin.com/in/soyeb-ganja
**Email**: soyeb.ganja@gmail.com
**GitHub**: SoyebGanja[https://github.com/soyebganja/ml-project-premium-prediction/blob/main/README.md]


---

**Note**: Make sure to have your trained model file (`resnet_model.pth`) in the `model/` directory before running the application.