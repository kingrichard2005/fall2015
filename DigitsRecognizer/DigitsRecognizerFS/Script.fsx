#load "Library1.fs"
open DigitsRecognizerFS
open System.IO
open System

// Define your library scripting code here
// Testing
// useful resource:
(*
    - http://dungpa.github.io/fsharp-cheatsheet/
    - http://fsharpforfunandprofit.com/troubleshooting-fsharp/
    - http://fsharpforfunandprofit.com/posts/overview-of-types-in-fsharp/
    - http://fsharpforfunandprofit.com/posts/defining-functions/
    - http://fsharpforfunandprofit.com/posts/match-expression/
    - http://fsharpforfunandprofit.com/posts/function-values-and-simple-values/
    - http://blogs.msdn.com/b/chrsmith/archive/2008/06/14/function-composition.aspx
*)
// text book example types and funcs
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

// Source files
let baseDirectory = __SOURCE_DIRECTORY__
let baseDirectory' = Directory.GetParent(baseDirectory)
let filePath = @"DigitsRecognizerTests\datasamples\digits\trainingsample.csv"
let fullPath = Path.Combine(baseDirectory'.FullName, filePath)
let trainingPath = fullPath

// text book example
// let trainingData = reader trainingPath

// Sandbox
type RawDataSource = { Path:string; includeHeaders: bool }
let to2DIntArray (aaInt:int [] []) =
    let dim1 = Array.length aaInt
    let dim2 = Array.length aaInt.[0]
    Array2D.init dim1 dim2 (fun i j -> aaInt.[i].[j]) 

let CsvStringtoIntArray (csvData:string) =
    let columns = csvData.Split(',')
    columns.[0..] |> Array.map int

let genericCsvReader (_source:RawDataSource) =
    (* path includeHeaders <- previously distinct input params were rolled up into custom type RawDataSource*) 
    match _source.includeHeaders with
    | false -> File.ReadAllLines _source.Path |> Seq.skip 1 |> Seq.toArray
    | _ -> File.ReadAllLines _source.Path |> Seq.toArray // all else take headers

let ``Read Csv Data To Int Array Then To 2D Array`` (_context:RawDataSource) =
    _context
    |> genericCsvReader
    |> Array.map CsvStringtoIntArray
    |> to2DIntArray

let options = { Path = trainingPath; includeHeaders = false }
let rawData = ``Read Csv Data To Int Array Then To 2D Array`` options
rawData.[0,0..]
//let sample = rawData.[0..1] |> Array.map CsvStringtoIntArray
//to2DIntArray sample
