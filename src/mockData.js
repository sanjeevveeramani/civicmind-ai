export const mockResult = {
  path_a_scores: {
    digitalInfrastructure: 78,
    dataReadiness: 62,
    aiGovernance: 45,
    workforceCapacity: 55,
    communityTrust: 38,
    serviceDelivery: 70,
  },

  arbitrator_result: [
    {
      dimension: "Community Trust",
      explanation:
        "Path B detected concerns not reflected in Path A scoring.",
    },
  ],

  gaps: {
    percentile: 42,

    quick_wins: [
      "Create public AI policy",
      "Run community workshops",
    ],

    medium_term: [
      "Train municipal staff",
      "Improve data collection",
    ],

    long_term: [
      "Establish AI governance board",
      "Develop AI readiness roadmap",
    ],
  },
};