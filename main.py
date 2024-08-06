import cv2
import matplotlib.pyplot as plt

def denoise_image(image_path):
    noisy_image = cv2.imread(image_path)
    noisy_image_rgb = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)

    gaussian_filter = cv2.GaussianBlur(noisy_image, (5,5), 0)
    gaussian_filter = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)

    median_filter = cv2.medianBlur(noisy_image, 5)
    median_filter = cv2.cvtColor(median_filter, cv2.COLOR_BGR2RGB)

    bilateral_filter = cv2.bilateralFilter(noisy_image, 9, 75, 75)
    bilateral_filter = cv2.cvtColor(bilateral_filter, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 1)
    plt.title('Noisy Image')
    plt.imshow(noisy_image_rgb)
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title('GaussianBlur Image')
    plt.imshow(gaussian_filter)
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title('medianBlur Image')
    plt.imshow(median_filter)
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title('bilateralFilter Image')
    plt.imshow(bilateral_filter)
    plt.axis('off')

    plt.show()


denoise_image('images.jpg')