package org.redhat.demo

import org.opencv.core.Mat
import org.opencv.core.MatOfRect
import org.opencv.core.Scalar
import org.opencv.imgproc.Imgproc


class Test {
  companion object {
    @JvmStatic
    fun main(args: Array<String>) {
      println("start")
    }
  }

  open fun detect(inputframe: Mat): Mat? {
    val mRgba = Mat()
    val mGrey = Mat()
    val faces = MatOfRect()
    inputframe.copyTo(mRgba)
    inputframe.copyTo(mGrey)
    Imgproc.cvtColor(mRgba, mGrey, Imgproc.COLOR_BGR2GRAY)
    Imgproc.equalizeHist(mGrey, mGrey)
    face_cascade.detectMultiScale(mGrey, faces)
    println(String.format("Detected %s face",
            faces.toArray().size))
    val smileDetections = MatOfRect()
    face_cascade1.detectMultiScale(mGrey, smileDetections)
    println(String.format("Detected %s smiles", smileDetections.toArray().size))
    for (rect in faces.toArray()) {
      val center = Point(rect.x + rect.width * 0.5, rect.y
              + rect.height * 0.5)
      Core.ellipse(mRgba, center, Size(rect.width * 0.5,
              rect.height * 0.5), 0, 0, 360, Scalar(255.0, 0.0, 255.0), 4,
              8, 0)
    }
    return mRgba
  }
}