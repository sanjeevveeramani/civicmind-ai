import { Card, Alert, Button, Tag, List } from "antd";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Cell,
} from "recharts";

const getColor = (score) =>
  score >= 70 ? "#27AE60" : score >= 40 ? "#F39C12" : "#E74C3C";

function ScoreResults({ data, setPage }) {
  const dimensions = data.scores.path_a.dimensions;
  const arbitrator = data.scores.arbitrator;
  const pathB = data.scores.path_b;

  return (
    <div>
      <Card title="Overall Score">
        <h1>{data.scores.path_a.overall_score}</h1>

        <Tag color={arbitrator.confidence === "high" ? "green" : "red"}>
          {arbitrator.confidence === "high"
            ? "HIGH CONFIDENCE"
            : "NEEDS REVIEW"}
        </Tag>
      </Card>

      <Card title="Dimension Scores" style={{ marginTop: 20 }}>
        <BarChart width={750} height={320} data={dimensions}>
          <XAxis dataKey="dimension" />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Bar dataKey="score">
            {dimensions.map((d, i) => (
              <Cell key={i} fill={getColor(d.score)} />
            ))}
          </Bar>
        </BarChart>
      </Card>

      <Card title="Divergence Alerts" style={{ marginTop: 20 }}>
        {arbitrator.divergences.length > 0 ? (
          arbitrator.divergences.map((item, index) => (
            <Alert
              key={index}
              type="error"
              message={`${item.dimension} Divergence`}
              description={
                <div>
                  <p>{item.explanation}</p>
                  <p>
                    <strong>Path A:</strong> {item.path_a_score} |{" "}
                    <strong>Path B:</strong> {item.path_b_score} |{" "}
                    <strong>Difference:</strong> {item.difference}
                  </p>
                </div>
              }
              showIcon
              style={{ marginBottom: 12 }}
            />
          ))
        ) : (
          <Alert
            type="success"
            message="No major divergence detected"
            description="Path A and Path B are aligned."
            showIcon
          />
        )}
      </Card>

      <Card title="Path B Recommendations" style={{ marginTop: 20 }}>
        <List
          dataSource={pathB.recommendations}
          renderItem={(item, index) => (
            <List.Item>
              <div>
                <strong>{item}</strong>
                <br />
                <em style={{ color: "#666" }}>
                  Non-AI alternative:{" "}
                  {pathB.non_ai_alternatives[index] ||
                    "Community-led manual review"}
                </em>
              </div>
            </List.Item>
          )}
        />
      </Card>

      <Card title="Similar Community Cases" style={{ marginTop: 20 }}>
        <List
          dataSource={pathB.similar_cases}
          renderItem={(item) => (
            <List.Item>
              <div>
                <strong>{item.name}</strong>
                <br />
                Outcome: {item.outcome}
                <br />
                <em>{item.relevance}</em>
              </div>
            </List.Item>
          )}
        />
      </Card>

      <Button
        type="primary"
        style={{ marginTop: 20 }}
        onClick={() => setPage("gaps")}
      >
        View Gap Analysis
      </Button>
    </div>
  );
}

export default ScoreResults;