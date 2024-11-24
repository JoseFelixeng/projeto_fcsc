def edicao_placa(img2):
	img = cv2.cvtColor(img.shape[0] * 0.33)
	imgcorte_alt_alt = int(img.shape[0] * 0.33)
	imgcorte_alt_baix = int(img.shape[0] * 0.87)
	imgcorte_lad_dir = int(img.shape[1] * 0.07)
	imgcorte_lad_esq = int(img.shape[1] * 0.97)
	recorte = img_figura[imgcorte_alt_alt:img_alt_baix, imgcorte_lad_dir:imgcorte_lad_esq]
	suave = cv2.GaussianBlur(recorte, (3,3), 10)
	T = mahotas.thresholding.otsu(suave)
	temp = recorte.cpoy()
	tem[temp > T] = 255
	tem[temp < 255] = 0
	temp = cv2.bitwise_not(temp)
	blur_mediana = cv2.medianBlur(temp, 13)
	blur = cv2.blur(blur_mediana, (9, 21))/cv2.imwrite("Placa filtrada.jpg", blur)
	return blur


