// import { CopilotSidebar } from "@copilotkit/react-ui"; 

// export default function Page() {
//   return (
//     <main>
//       <h1>Mini Mind</h1>
//       <CopilotSidebar />
//     </main>
//   );
// }


"use client";

import { useFrontendTool, useRenderToolCall } from "@copilotkit/react-core";
import { CopilotSidebar, CopilotKitCSSProperties } from "@copilotkit/react-ui";
import { useState } from "react";

export default function Page() {
  const [background, setBackground] = useState("#6366f1");

  // Frontend tool for changing background
  useFrontendTool({
    name: "change_background",
    description: "Change the background color of the chat.",
    parameters: [
      {
        name: "background",
        type: "string",
        description: "The background color or gradient. Prefer gradients.",
        required: true,
      },
    ],
    handler: async ({ background }) => {
      setBackground(background);
      return `Background changed to ${background}`;
    },
  });

  // Render tool call for bar_chat_data visualization
  useRenderToolCall({
    name: "bar_chat_data",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-blue-50 rounded-lg">
            <p className="text-sm text-blue-600">
              Creating bar chart: {args.title}...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const chartData = result;
        const maxValue = Math.max(...Object.values(chartData.data).map(v => v as number));

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-3">📊 {chartData.title}</h3>
            <p className="text-sm text-gray-600 mb-4">{chartData.summary}</p>
            <div className="space-y-3">
              {Object.entries(chartData.data).map(([day, tip]) => (
                <div key={day} className="flex items-center gap-3">
                  <span className="w-16 text-sm font-medium text-gray-700">{day}</span>
                  <div className="flex-1 flex items-center gap-2">
                    <div className="flex-1 h-8 bg-gray-200 rounded overflow-hidden">
                      <div
                        className="h-full bg-blue-500 flex items-center justify-end pr-2"
                        style={{ width: `${((tip as number) / maxValue) * 100}%` }}
                      >
                        <span className="text-xs text-white font-semibold">
                          ${(tip as number).toFixed(2)}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-3 pt-3 border-t text-xs text-gray-500">
              <span>{chartData.x_label} vs {chartData.y_label}</span>
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for scatter_plot_data visualization
  useRenderToolCall({
    name: "scatter_plot_data",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-purple-50 rounded-lg">
            <p className="text-sm text-purple-600">
              Creating scatter plot: {args.title}...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const plotData = result;

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-3">📈 {plotData.title}</h3>
            <p className="text-sm text-gray-600 mb-4">{plotData.summary}</p>
            <div className="bg-gray-50 p-4 rounded">
              <p className="text-sm text-gray-700 mb-2">
                <strong>Data Points:</strong> {plotData.data.days.length} records
              </p>
              <p className="text-sm text-gray-700">
                <strong>Axes:</strong> {plotData.x_label} (X) vs {plotData.y_label} (Y)
              </p>
              <p className="text-sm text-gray-700 mt-2">
                <strong>Tip Range:</strong> $
                {Math.min(...plotData.data.tips).toFixed(2)} - $
                {Math.max(...plotData.data.tips).toFixed(2)}
              </p>
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for sentiment analysis
  useRenderToolCall({
    name: "sentiment_analysis",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-green-50 rounded-lg">
            <p className="text-sm text-green-600">
              Analyzing sentiment{args?.sentence ? ` of: "${args.sentence.substring(0, 50)}..."` : "..."}
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const sentiment = typeof result === 'string' ? result.toLowerCase().trim() : '';
        const sentimentEmoji = sentiment === 'positive' ? '😊' : sentiment === 'negative' ? '😞' : '😐';
        const sentimentColor = sentiment === 'positive' ? 'text-green-600' : sentiment === 'negative' ? 'text-red-600' : 'text-gray-600';

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              😊 Sentiment Analysis Results
            </h3>
            <div className="flex items-center justify-center p-6">
              <div className="text-center">
                <div className="text-6xl mb-3">{sentimentEmoji}</div>
                <div className={`text-2xl font-bold ${sentimentColor} capitalize`}>
                  {sentiment || 'Unknown'}
                </div>
              </div>
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for keyword extraction
  useRenderToolCall({
    name: "extract_keywords",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-yellow-50 rounded-lg">
            <p className="text-sm text-yellow-600">
              Extracting keywords from text...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const keywords = result;
        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              🔑 Extracted Keywords
            </h3>
            <div className="flex flex-wrap gap-2">
              {Object.entries(keywords).map(([word, score]) => (
                <span
                  key={word}
                  className="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full text-sm"
                >
                  {word}{" "}
                  <span className="text-xs opacity-75">
                    ({typeof score === "number" ? score.toFixed(3) : score})
                  </span>
                </span>
              ))}
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for emotion detection
  useRenderToolCall({
    name: "detect_emotions",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-pink-50 rounded-lg">
            <p className="text-sm text-pink-600">
              Detecting emotions in text...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const emotions = result;
        const emotionIcons: Record<string, string> = {
          joy: "😄",
          sadness: "😢",
          anger: "😠",
          fear: "😨",
          surprise: "😲",
          neutral: "😐",
        };

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              🎭 Emotion Detection Results
            </h3>
            <div className="space-y-2 text-sm">
              {Object.entries(emotions).map(([emotion, score]) => (
                <div key={emotion} className="flex justify-between items-center">
                  <span>
                    {emotionIcons[emotion]} {emotion.charAt(0).toUpperCase() + emotion.slice(1)}:
                  </span>
                  <div className="flex items-center gap-2">
                    <div className="w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-pink-500"
                        style={{ width: `${(score as number) * 100}%` }}
                      ></div>
                    </div>
                    <span className="font-semibold w-12 text-right">
                      {((score as number) * 100).toFixed(1)}%
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for entity extraction
  useRenderToolCall({
    name: "extract_entities",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-indigo-50 rounded-lg">
            <p className="text-sm text-indigo-600">
              Extracting named entities from text...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const entities = result;
        const categoryColors: Record<string, string> = {
          people: "bg-blue-100 text-blue-800",
          places: "bg-green-100 text-green-800",
          organizations: "bg-purple-100 text-purple-800",
          dates: "bg-orange-100 text-orange-800",
          other: "bg-gray-100 text-gray-800",
        };
        const categoryEmojis: Record<string, string> = {
          people: "👤",
          places: "📍",
          organizations: "🏢",
          dates: "📅",
          other: "🔖",
        };

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              🏷️ Named Entity Recognition
            </h3>
            <div className="space-y-3 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-600">Total Entities:</span>
                <span className="font-semibold">{entities.total_entities || 0}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Unique Entities:</span>
                <span className="font-semibold">{entities.unique_entities || 0}</span>
              </div>
              {entities.entities_by_type && (
                <div className="space-y-3">
                  {Object.entries(entities.entities_by_type).map(([category, items]: [string, any]) =>
                    items && items.length > 0 ? (
                      <div key={category}>
                        <p className="text-gray-600 mb-2 capitalize">
                          {categoryEmojis[category] || "🔖"} {category}:
                        </p>
                        <div className="flex flex-wrap gap-2">
                          {items.map((entity: string, idx: number) => (
                            <span
                              key={idx}
                              className={`px-2 py-1 rounded text-xs ${categoryColors[category] || categoryColors.other}`}
                            >
                              {entity}
                            </span>
                          ))}
                        </div>
                      </div>
                    ) : null
                  )}
                </div>
              )}
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for readability analysis
  useRenderToolCall({
    name: "analyze_readability",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-orange-50 rounded-lg">
            <p className="text-sm text-orange-600">
              Analyzing text readability...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const readability = result;
        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              📖 Readability Analysis
            </h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-600">Word Count:</span>
                <span className="font-semibold">{readability.word_count}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Sentence Count:</span>
                <span className="font-semibold">{readability.sentence_count}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Avg Word Length:</span>
                <span className="font-semibold">{readability.avg_word_length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Avg Sentence Length:</span>
                <span className="font-semibold">{readability.avg_sentence_length}</span>
              </div>
              <div className="mt-3 pt-3 border-t">
                <div className="flex justify-between items-center">
                  <span className="text-gray-600">Readability Score:</span>
                  <span className="font-bold text-lg">{readability.readability_score}</span>
                </div>
                <div className="mt-1">
                  <span
                    className={`px-3 py-1 rounded-full text-xs font-semibold ${
                      readability.difficulty_level === "Easy"
                        ? "bg-green-100 text-green-800"
                        : readability.difficulty_level === "Medium"
                        ? "bg-yellow-100 text-yellow-800"
                        : "bg-red-100 text-red-800"
                    }`}
                  >
                    {readability.difficulty_level}
                  </span>
                </div>
              </div>
            </div>
          </div>
        );
      }

      return null;
    },
  });

  // Render tool call for word frequency
  useRenderToolCall({
    name: "word_frequency",
    render: ({ status, args, result }) => {
      if (status === "executing") {
        return (
          <div className="p-4 bg-teal-50 rounded-lg">
            <p className="text-sm text-teal-600">
              Analyzing word frequency...
            </p>
          </div>
        );
      }

      if (status === "complete" && result) {
        const frequencies = result;
        const maxFreq = Math.max(...Object.values(frequencies).map(v => v as number));

        return (
          <div className="p-4 bg-white border rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">
              📊 Word Frequency Analysis
            </h3>
            <div className="space-y-2 text-sm">
              {Object.entries(frequencies).map(([word, count]) => (
                <div key={word} className="flex items-center gap-2">
                  <span className="w-24 text-gray-700">{word}:</span>
                  <div className="flex-1 flex items-center gap-2">
                    <div className="flex-1 h-6 bg-gray-200 rounded overflow-hidden">
                      <div
                        className="h-full bg-teal-500 flex items-center justify-end pr-2"
                        style={{ width: `${((count as number) / maxFreq) * 100}%` }}
                      >
                        <span className="text-xs text-white font-semibold">{count}</span>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        );
      }

      return null;
    },
  });

  return (
    <main
      style={{
        background,
        transition: "background 0.3s ease",
      }}
      className="h-screen"
    >
      <CopilotSidebar />
    </main>
  );
}