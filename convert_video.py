import imageio

input_path = r"C:\Users\Munshi Arman Rahim\.gemini\antigravity\brain\bb10e1ed-d874-40f0-9f1a-23984159d8f4\indian_food_analysis_demo_1779964169961.webp"
output_path = r"C:\Users\Munshi Arman Rahim\OneDrive\Desktop\Python deliverables\Code file\indian-food-cuisine-analysis\demo_video.mp4"

print("Starting conversion...")
try:
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data().get('fps', 30)
    
    writer = imageio.get_writer(output_path, fps=fps, codec='libx264')
    
    for i, frame in enumerate(reader):
        writer.append_data(frame)
        
    writer.close()
    print(f"Successfully converted video to {output_path}")
except Exception as e:
    print(f"Error during conversion: {e}")
