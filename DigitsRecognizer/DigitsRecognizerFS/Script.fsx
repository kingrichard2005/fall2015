#load "Library1.fs"
open DigitsRecognizerFS
open System.IO
open System

// Define your library scripting code here
// Testing
let x = 42
let y = x + 100

type Observation = { Label:string; Pixels: int[] }

let toObservation (csvData:string) =
    let columns = csvData.Split(',')
    let label = columns.[0]
    let pixels = columns.[1..] |> Array.map int
    { Label = label; Pixels = pixels }

let reader path =
    let data = File.ReadAllLines path
    data.[1..]
    |> Array.map toObservation

let baseDirectory = __SOURCE_DIRECTORY__
let baseDirectory' = Directory.GetParent(baseDirectory)
let filePath = @"DigitsRecognizerTests\datasamples\digits\trainingsample.csv"
let fullPath = Path.Combine(baseDirectory'.FullName, filePath)
let trainingPath = fullPath
let trainingData = reader trainingPath