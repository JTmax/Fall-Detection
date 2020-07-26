# opencv requires at least 2 images to carry out background subtraction

import cv2
import glob
import os

def backsub(impath, subtractor):
	im = cv2.imread(impath)
	frame = subtractor.apply(im)
	return frame


def backgroundSub():
	mog2 = cv2.createBackgroundSubtractorMOG2()
	root = '/home/taryar/deepLearning/research/victor/data/real'
	test_path_F = root + '/Fall*'
	Fall_dir_list = glob.glob(test_path_F)
	print(len(Fall_dir_list))

	i = 1
	for Fall_dir in Fall_dir_list:
		frames = sorted(glob.glob(Fall_dir + '/file_*.png'))
		print(frames)

		save_path = root + '/subtracted/Fall{}'.format(i)
		
		j = 0
		for frame in frames:
			frame_filled = backsub(frame, mog2)

			#frame_base = os.path.basename(frame)

			save_path_fr = save_path + '/' + 'file_{}.png'.format(j)
			print(save_path_fr)
			j += 1

			cv2.imwrite(save_path_fr, frame_filled)
		#break

		i += 1

if __name__ == "__main__":
	backgroundSub()