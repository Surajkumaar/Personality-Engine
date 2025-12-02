// script.js - Frontend logic for Memory + Personality Engine

function memoryApp() {
    return {
        // Data
        chatMessages: '',
        sampleReply: 'Start by collecting your dataset and then preprocess the images for better results.',
        selectedStyle: 'calm_mentor',
        loading: false,
        error: null,
        memoryResults: null,
        transformResult: null,
        comparisonResult: null,
        
        // API base URL - automatically detects environment
        apiUrl: window.location.hostname === 'localhost' ? 
            'http://127.0.0.1:8000' : 
            'https://your-backend-url.railway.app',  // Update with your deployed backend URL

        // Load sample messages for demo
        loadSampleMessages() {
            this.chatMessages = `I love Python and VSCode for coding.
I'm worried I won't finish the assignment on time.
Contact: alex.smith@example.com
My number is 9876543210
I prefer Colab for quick GPU testing.
I enjoy working on cybersecurity projects.
I'm happy with fast iterations in development.
I'm sad about delays sometimes in my projects.
Living in San Francisco, California.
I use Git and GitHub for version control.
No experience in mobile conversion yet.
I like DenseNet169 for transfer learning.
I use Obsidian to save my research notes.
I worry about dataset size limitations.
I feel excited when experiments succeed.
I don't like noisy labels in my datasets.
I love writing clean, maintainable code.
My mentor is Dr. Sarah Johnson.
I want to deploy models on Hugging Face Spaces.
I prefer concise, direct replies over long explanations.
I enjoy using Tailwind CSS for frontend work.
I worked on the ThreatNet security project last year.
I have intermediate ethical hacking skills.
I want to run models on-device with TFLite optimization.
I use VS Code on Ubuntu for my main development.
I enjoy data analysis tasks and visualization.
I sometimes feel frustrated with environment setup issues.
I prefer technical answers without too much hand-holding.
My name is Alex and I'm a CS graduate student.
I study machine learning at Stanford University.`;
        },

        // Extract memory from chat messages
        async extractMemory() {
            try {
                this.loading = true;
                this.error = null;
                
                const messages = this.chatMessages.split('\n').filter(msg => msg.trim());
                
                const response = await fetch(`${this.apiUrl}/extract`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ messages: messages })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                this.memoryResults = data;
                
                // Clear previous results when new memory is extracted
                this.transformResult = null;
                this.comparisonResult = null;
                
            } catch (error) {
                console.error('Error extracting memory:', error);
                this.error = `Failed to extract memory: ${error.message}. Make sure the backend server is running on ${this.apiUrl}`;
            } finally {
                this.loading = false;
            }
        },

        // Transform reply with selected personality
        async transformReply() {
            try {
                this.loading = true;
                this.error = null;
                
                const messages = this.chatMessages.split('\n').filter(msg => msg.trim());
                
                const response = await fetch(`${this.apiUrl}/transform`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        messages: messages,
                        style: this.selectedStyle,
                        sample_reply: this.sampleReply
                    })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                this.transformResult = data;
                this.comparisonResult = null; // Clear comparison when showing single result
                
            } catch (error) {
                console.error('Error transforming reply:', error);
                this.error = `Failed to transform reply: ${error.message}`;
            } finally {
                this.loading = false;
            }
        },

        // Compare all personality styles
        async comparePersonalities() {
            try {
                this.loading = true;
                this.error = null;
                
                const messages = this.chatMessages.split('\n').filter(msg => msg.trim());
                
                const response = await fetch(`${this.apiUrl}/compare`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        messages: messages,
                        sample_reply: this.sampleReply
                    })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                this.comparisonResult = data;
                this.transformResult = null; // Clear single result when showing comparison
                
            } catch (error) {
                console.error('Error comparing personalities:', error);
                this.error = `Failed to compare personalities: ${error.message}`;
            } finally {
                this.loading = false;
            }
        },

        // Initialize app
        init() {
            // Check if backend is running
            this.checkBackendStatus();
        },

        async checkBackendStatus() {
            try {
                const response = await fetch(`${this.apiUrl}/`);
                if (response.ok) {
                    console.log('Backend is running successfully');
                }
            } catch (error) {
                console.warn('Backend may not be running. Please start it with: uvicorn app:app --host 127.0.0.1 --port 8000');
                this.error = 'Backend server not detected. Please start it with: uvicorn app:app --host 127.0.0.1 --port 8000';
            }
        }
    };
}