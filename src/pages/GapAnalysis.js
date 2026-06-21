import { Card, Collapse, Button, Table } from "antd";

function GapAnalysis({ data, setPage }) {
  const plan = data.gaps.action_plan;
  const percentiles = data.gaps.percentiles || {};

  const percentileRows = Object.entries(percentiles).map(([dimension, value]) => ({
    key: dimension,
    dimension,
    percentile: `${value}%`,
  }));

  const weightRows = [
    { key: "1", dimension: "Infrastructure", weight: "20%" },
    { key: "2", dimension: "Workforce", weight: "20%" },
    { key: "3", dimension: "Data Maturity", weight: "25%" },
    { key: "4", dimension: "Governance", weight: "15%" },
    { key: "5", dimension: "Ethics", weight: "10%" },
    { key: "6", dimension: "Public Trust", weight: "10%" },
  ];

  return (
    <div>
      <Card title="Peer Comparison">
        <Table
          dataSource={percentileRows}
          pagination={false}
          columns={[
            { title: "Dimension", dataIndex: "dimension" },
            { title: "Percentile vs Peers", dataIndex: "percentile" },
          ]}
        />
      </Card>

      <Card title="Gap Analysis" style={{ marginTop: 20 }}>
        <Collapse
          items={[
            {
              key: "1",
              label: "Quick Wins (0–3 months)",
              children: (
                <ul>
                  {plan.quick_wins.map((x, i) => (
                    <li key={i}>{x}</li>
                  ))}
                </ul>
              ),
            },
            {
              key: "2",
              label: "Medium-Term Actions (3–12 months)",
              children: (
                <ul>
                  {plan.medium_term.map((x, i) => (
                    <li key={i}>{x}</li>
                  ))}
                </ul>
              ),
            },
            {
              key: "3",
              label: "Long-Term Strategy (1–3 years)",
              children: (
                <ul>
                  {plan.long_term.map((x, i) => (
                    <li key={i}>{x}</li>
                  ))}
                </ul>
              ),
            },
          ]}
        />
      </Card>

      <Card title="Scoring Transparency" style={{ marginTop: 20 }}>
        <Table
          dataSource={weightRows}
          pagination={false}
          columns={[
            { title: "Dimension", dataIndex: "dimension" },
            { title: "Weight", dataIndex: "weight" },
          ]}
        />

        <p style={{ marginTop: 16 }}>
          <strong>Sources:</strong> OECD AI Policy Observatory; Stanford HAI AI
          Index.
        </p>
      </Card>

      <Button style={{ marginTop: 20 }} onClick={() => setPage("results")}>
        Back to Results
      </Button>

      <Button style={{ marginTop: 20, marginLeft: 12 }} onClick={() => setPage("intake")}>
        Start Over
      </Button>
    </div>
  );
}

export default GapAnalysis;